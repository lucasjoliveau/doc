# ORM API

  * [Changelog](orm/changelog)

## Models

Model fields are defined as attributes on the model itself:

    
    
    from odoo import models, fields
    class AModel(models.Model):
        _name = 'a.model.name'
    
        field1 = fields.Char()
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>this means you cannot define a field and a method with the same
name, the last one will silently overwrite the former ones.</p>
</div>

By default, the field’s label (user-visible name) is a capitalized version of
the field name, this can be overridden with the `string` parameter.

    
    
    field2 = fields.Integer(string="Field Label")
    

For the list of field types and parameters, see the fields reference.

Default values are defined as parameters on fields, either as a value:

    
    
    name = fields.Char(default="a value")
    

or as a function called to compute the default value, which should return that
value:

    
    
    def _default_name(self):
        return self.get_value()
    
    name = fields.Char(default=lambda self: self._default_name())
    

API

### AbstractModel

### Model

### TransientModel

## Fields

### Basic Fields

### Advanced Fields

#### Date(time) Fields

`Dates` and `Datetimes` are very important fields in any kind of business
application. Their misuse can create invisible yet painful bugs, this section
aims to provide Konvergo ERP developers with the knowledge required to avoid misusing
these fields.

When assigning a value to a Date/Datetime field, the following options are
valid:

  * A `date` or `datetime` object.

  * A string in the proper server format:

    * `YYYY-MM-DD` for `Date` fields,

    * `YYYY-MM-DD HH:MM:SS` for `Datetime` fields.

  * `False` or `None`.

The Date and Datetime fields class have helper methods to attempt conversion
into a compatible type:

  * `to_date()` will convert to a [`datetime.date`](https://docs.python.org/3/library/datetime#datetime.date "\(disponible dans Python v3.12\)")

  * `to_datetime()` will convert to a [`datetime.datetime`](https://docs.python.org/3/library/datetime#datetime.datetime "\(disponible dans Python v3.12\)").

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>

Date / Datetime comparison best practices:

  * Date fields can **only** be compared to date objects.

  * Datetime fields can **only** be compared to datetime objects.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Strings representing dates and datetimes can be compared
between each other, however the result may not be the expected
result, as a datetime string will always be greater than a
date string, therefore this practice is <b>heavily</b>
discouraged.</p>
</div>

Common operations with dates and datetimes such as addition, subtraction or
fetching the start/end of a period are exposed through both `Date` and
`Datetime`. These helpers are also available by importing
`odoo.tools.date_utils`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Timezones</p>
<p>Datetime fields are stored as <code>timestamp without timezone</code> columns in the database and are stored
in the UTC timezone. This is by design, as it makes the Konvergo ERP database independent from the timezone
of the hosting server system. Timezone conversion is managed entirely by the client side.</p>
</div>

#### Relational Fields

#### Pseudo-relational fields

#### Computed Fields

Fields can be computed (instead of read straight from the database) using the
`compute` parameter. **It must assign the computed value to the field**. If it
uses the values of other _fields_ , it should specify those fields using
`depends()`.

    
    
    from odoo import api
    total = fields.Float(compute='_compute_total')
    
    @api.depends('value', 'tax')
    def _compute_total(self):
        for record in self:
            record.total = record.value + record.value * record.tax
    

  * dependencies can be dotted paths when using sub-fields:
    
        @api.depends('line_ids.value')
    def _compute_total(self):
        for record in self:
            record.total = sum(line.value for line in record.line_ids)
    

  * computed fields are not stored by default, they are computed and returned when requested. Setting `store=True` will store them in the database and automatically enable searching.

  * searching on a computed field can also be enabled by setting the `search` parameter. The value is a method name returning a Search domains.
    
        upper_name = field.Char(compute='_compute_upper', search='_search_upper')
    
    def _search_upper(self, operator, value):
        if operator == 'like':
            operator = 'ilike'
        return [('name', operator, value)]
    

The search method is invoked when processing domains before doing an actual
search on the model. It must return a domain equivalent to the condition:
`field operator value`.

  * Computed fields are readonly by default. To allow _setting_ values on a computed field, use the `inverse` parameter. It is the name of a function reversing the computation and setting the relevant fields:
    
        document = fields.Char(compute='_get_document', inverse='_set_document')
    
    def _get_document(self):
        for record in self:
            with open(record.get_document_path) as f:
                record.document = f.read()
    def _set_document(self):
        for record in self:
            if not record.document: continue
            with open(record.get_document_path()) as f:
                f.write(record.document)
    

  * multiple fields can be computed at the same time by the same method, just use the same method on all fields and set all of them:
    
        discount_value = fields.Float(compute='_apply_discount')
    total = fields.Float(compute='_apply_discount')
    
    @api.depends('value', 'discount')
    def _apply_discount(self):
        for record in self:
            # compute actual discount from discount percentage
            discount = record.value * record.discount
            record.discount_value = discount
            record.total = record.value - discount
    

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>While it is possible to use the same compute method for multiple
fields, it is not recommended to do the same for the inverse
method.</p>
<p>During the computation of the inverse, <b>all</b> fields that use
said inverse are protected, meaning that they can’t be computed,
even if their value is not in the cache.</p>
<p>If any of those fields is accessed and its value is not in cache,
the ORM will simply return a default value of <code>False</code> for these fields.
This means that the value of the inverse fields (other than the one
triggering the inverse method) may not give their correct value and
this will probably break the expected behavior of the inverse method.</p>
</div>

#### Related fields

A special case of computed fields are _related_ (proxy) fields, which provide
the value of a sub-field on the current record. They are defined by setting
the `related` parameter and like regular computed fields they can be stored:

    
    
    nickname = fields.Char(related='user_id.partner_id.name', store=True)
    

The value of a related field is given by following a sequence of relational
fields and reading a field on the reached model. The complete sequence of
fields to traverse is specified by the `related` attribute.

Some field attributes are automatically copied from the source field if they
are not redefined: `string`, `help`, `required` (only if all fields in the
sequence are required), `groups`, `digits`, `size`, `translate`, `sanitize`,
`selection`, `comodel_name`, `domain`, `context`. All semantic-free attributes
are copied from the source field.

By default, related fields are:

  * not stored

  * not copied

  * readonly

  * computed in superuser mode

Add the attribute `store=True` to make it stored, just like computed fields.
Related fields are automatically recomputed when their dependencies are
modified.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>You can specify precise field dependencies if you don’t want
the related field to be recomputed on any dependency change:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">nickname</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">Char</span><span class="p">(</span>
    <span class="n">related</span><span class="o">=</span><span class="s1">'partner_id.name'</span><span class="p">,</span> <span class="n">store</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">depends</span><span class="o">=</span><span class="p">[</span><span class="s1">'partner_id'</span><span class="p">])</span>
<span class="c1"># The nickname will only be recomputed when the partner_id</span>
<span class="c1"># is modified, not when the name is modified on the partner.</span>
</pre></div>
</div>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>You cannot chain <code>Many2many</code> or <code>One2many</code> fields in <code>related</code> fields dependencies.</p>
<p><code>related</code> can be used to refer to a <code>One2many</code> or
<code>Many2many</code> field on another model on the
condition that it’s done through a <code>Many2one</code> relation on the current model.
<code>One2many</code> and <code>Many2many</code> are not supported and the results will not be
aggregated correctly:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">m2o_id</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">Many2one</span><span class="p">()</span>
<span class="n">m2m_ids</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">Many2many</span><span class="p">()</span>
<span class="n">o2m_ids</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">One2many</span><span class="p">()</span>

<span class="c1"># Supported</span>
<span class="n">d_ids</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">Many2many</span><span class="p">(</span><span class="n">related</span><span class="o">=</span><span class="s2">"m2o_id.m2m_ids"</span><span class="p">)</span>
<span class="n">e_ids</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">One2many</span><span class="p">(</span><span class="n">related</span><span class="o">=</span><span class="s2">"m2o_id.o2m_ids"</span><span class="p">)</span>

<span class="c1"># Won't work: use a custom Many2many computed field instead</span>
<span class="n">f_ids</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">Many2many</span><span class="p">(</span><span class="n">related</span><span class="o">=</span><span class="s2">"m2m_ids.m2m_ids"</span><span class="p">)</span>
<span class="n">g_ids</span> <span class="o">=</span> <span class="n">fields</span><span class="o">.</span><span class="n">One2many</span><span class="p">(</span><span class="n">related</span><span class="o">=</span><span class="s2">"o2m_ids.o2m_ids"</span><span class="p">)</span>
</pre></div>
</div>
</div>

### Automatic fields

Model.id

    

Identifier `field`

If length of current recordset is 1, return id of unique record in it.

Raise an Error otherwise.

#### Access Log fields

These fields are automatically set and updated if `_log_access` is enabled. It
can be disabled to avoid creating or updating those fields on tables for which
they are not useful.

By default, `_log_access` is set to the same value as `_auto`

Model.create_date

    

Stores when the record was created, `Datetime`

Model.create_uid

    

Stores _who_ created the record, `Many2one` to a `res.users`.

Model.write_date

    

Stores when the record was last updated, `Datetime`

Model.write_uid

    

Stores who last updated the record, `Many2one` to a `res.users`.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p><code>_log_access</code> <em>must</em> be enabled on
<code>TransientModel</code>.</p>
</div>

### Reserved Field names

A few field names are reserved for pre-defined behaviors beyond that of
automated fields. They should be defined on a model when the related behavior
is desired:

Model.name

    

default value for `_rec_name`, used to display records in context where a
representative « naming » is necessary.

`Char`

Model.active

    

toggles the global visibility of the record, if `active` is set to `False` the
record is invisible in most searches and listing.

`Boolean`

Special methods:

Model.state

    

lifecycle stages of the object, used by the `states` attribute on `fields`.

`Selection`

Model.parent_id

    

default_value of `_parent_name`, used to organize records in a tree structure
and enables the `child_of` and `parent_of` operators in domains.

`Many2one`

Model.parent_path

    

When `_parent_store` is set to True, used to store a value reflecting the tree
structure of `_parent_name`, and to optimize the operators `child_of` and
`parent_of` in search domains. It must be declared with `index=True` for
proper operation.

`Char`

Model.company_id

    

Main field name used for Konvergo ERP multi-company behavior.

Used by `:meth:~odoo.models._check_company` to check multi company
consistency. Defines whether a record is shared between companies (no value)
or only accessible by the users of a given company.

`Many2one` :type: `res_company`

## Recordsets

Interactions with models and records are performed through recordsets, an
ordered collection of records of the same model.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Contrary to what the name implies, it is currently possible for
recordsets to contain duplicates. This may change in the future.</p>
</div>

Methods defined on a model are executed on a recordset, and their `self` is a
recordset:

    
    
    class AModel(models.Model):
        _name = 'a.model'
        def a_method(self):
            # self can be anything between 0 records and all records in the
            # database
            self.do_operation()
    

Iterating on a recordset will yield new sets of _a single record_ («
singletons »), much like iterating on a Python string yields strings of a
single characters:

    
    
    def do_operation(self):
        print(self) # => a.model(1, 2, 3, 4, 5)
        for record in self:
            print(record) # => a.model(1), then a.model(2), then a.model(3), ...
    

### Field access

Recordsets provide an « Active Record » interface: model fields can be read
and written directly from the record as attributes.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When accessing non-relational fields on a recordset of potentially multiple
records, use <code>mapped()</code>:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">total_qty</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">mapped</span><span class="p">(</span><span class="s1">'qty'</span><span class="p">))</span>
</pre></div>
</div>
</div>

Field values can also be accessed like dict items, which is more elegant and
safer than `getattr()` for dynamic field names. Setting a field’s value
triggers an update to the database:

    
    
    >>> record.name
    Example Name
    >>> record.company_id.name
    Company Name
    >>> record.name = "Bob"
    >>> field = "name"
    >>> record[field]
    Bob
    

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>0

Accessing a relational field (`Many2one`, `One2many`, `Many2many`) _always_
returns a recordset, empty if the field is not set.

### Record cache and prefetching

Konvergo ERP maintains a cache for the fields of the records, so that not every field
access issues a database request, which would be terrible for performance. The
following example queries the database only for the first statement:

    
    
    record.name             # first access reads value from database
    record.name             # second access gets value from cache
    

To avoid reading one field on one record at a time, Konvergo ERP _prefetches_ records
and fields following some heuristics to get good performance. Once a field
must be read on a given record, the ORM actually reads that field on a larger
recordset, and stores the returned values in cache for later use. The
prefetched recordset is usually the recordset from which the record comes by
iteration. Moreover, all simple stored fields (boolean, integer, float, char,
text, date, datetime, selection, many2one) are fetched altogether; they
correspond to the columns of the model’s table, and are fetched efficiently in
the same query.

Consider the following example, where `partners` is a recordset of 1000
records. Without prefetching, the loop would make 2000 queries to the
database. With prefetching, only one query is made:

    
    
    for partner in partners:
        print partner.name          # first pass prefetches 'name' and 'lang'
                                    # (and other fields) on all 'partners'
        print partner.lang
    

The prefetching also works on _secondary records_ : when relational fields are
read, their values (which are records) are subscribed for future prefetching.
Accessing one of those secondary records prefetches all secondary records from
the same model. This makes the following example generate only two queries,
one for partners and one for countries:

    
    
    countries = set()
    for partner in partners:
        country = partner.country_id        # first pass prefetches all partners
        countries.add(country.name)         # first pass prefetches all countries
    

## Method decorators

## Environment

    
    
    >>> records.env
    <Environment object ...>
    >>> records.env.uid
    3
    >>> records.env.user
    res.user(3)
    >>> records.env.cr
    <Cursor object ...>
    

When creating a recordset from an other recordset, the environment is
inherited. The environment can be used to get an empty recordset in an other
model, and query that model:

    
    
    >>> self.env['res.partner']
    res.partner()
    >>> self.env['res.partner'].search([('is_company', '=', True), ('customer', '=', True)])
    res.partner(7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74)
    

Some lazy properties are available to access the environment (contextual)
data:

### Useful environment methods

### Altering the environment

### SQL Execution

The `cr` attribute on environments is the cursor for the current database
transaction and allows executing SQL directly, either for queries which are
difficult to express using the ORM (e.g. complex joins) or for performance
reasons:

    
    
    self.env.cr.execute("some_sql", params)
    

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>1

One important thing to know about models is that they don’t necessarily
perform database updates right away. Indeed, for performance reasons, the
framework delays the recomputation of fields after modifying records. And some
database updates are delayed, too. Therefore, before querying the database,
one has to make sure that it contains the relevant data for the query. This
operation is called _flushing_ and performs the expected database updates.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>2

Before every SQL query, one has to flush the data needed for that query. There
are three levels for flushing, each with its own API. One can flush either
everything, all the records of a model, or some specific records. Because
delaying updates improves performance in general, we recommend to be
_specific_ when flushing.

Because models use the same cursor and the `Environment` holds various caches,
these caches must be invalidated when _altering_ the database in raw SQL, or
further uses of models may become incoherent. It is necessary to clear caches
when using `CREATE`, `UPDATE` or `DELETE` in SQL, but not `SELECT` (which
simply reads the database).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>3

Just like flushing, one can invalidate either the whole cache, the cache of
all the records of a model, or the cache of specific records. One can even
invalidate specific fields on some records or all records of a model. As the
cache improves performance in general, we recommend to be _specific_ when
invalidating.

The methods above keep the caches and the database consistent with each other.
However, if computed field dependencies have been modified in the database,
one has to inform the models for the computed fields to be recomputed. The
only thing the framework needs to know is _what_ fields have changed on
_which_ records.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>4

One has to figure out which records have been modified. There are many ways to
do this, possibly involving extra SQL queries. In the example above, we take
advantage of the `RETURNING` clause of PostgreSQL to retrieve the information
without an extra query. After making the cache consistent by invalidation,
invoke the method `modified` on the modified records with the fields that have
been updated.

## Common ORM methods

### Create/update

### Search/Read

#### Fields

#### Search domains

A domain is a list of criteria, each criterion being a triple (either a `list`
or a `tuple`) of `(field_name, operator, value)` where:

  * `field_name` (`str`)
    

a field name of the current model, or a relationship traversal through a
`Many2one` using dot-notation e.g. `'street'` or `'partner_id.country'`

  * `operator` (`str`)
    

an operator used to compare the `field_name` with the `value`. Valid operators
are:

`=`

    

equals to

`!=`

    

not equals to

`>`

    

greater than

`>=`

    

greater than or equal to

`<`

    

less than

`<=`

    

less than or equal to

`=?`

    

unset or equals to (returns true if `value` is either `None` or `False`,
otherwise behaves like `=`)

`=like`

    

matches `field_name` against the `value` pattern. An underscore `_` in the
pattern stands for (matches) any single character; a percent sign `%` matches
any string of zero or more characters.

`like`

    

matches `field_name` against the `%value%` pattern. Similar to `=like` but
wraps `value` with “%” before matching

`not like`

    

doesn’t match against the `%value%` pattern

`ilike`

    

case insensitive `like`

`not ilike`

    

case insensitive `not like`

`=ilike`

    

case insensitive `=like`

`in`

    

is equal to any of the items from `value`, `value` should be a list of items

`not in`

    

is unequal to all of the items from `value`

`child_of`

    

is a child (descendant) of a `value` record (value can be either one item or a
list of items).

Takes the semantics of the model into account (i.e following the relationship
field named by `_parent_name`).

`parent_of`

    

is a parent (ascendant) of a `value` record (value can be either one item or a
list of items).

Takes the semantics of the model into account (i.e following the relationship
field named by `_parent_name`).

  * `value`
    

variable type, must be comparable (through `operator`) to the named field.

Domain criteria can be combined using logical operators in _prefix_ form:

`'&'`

    

logical _AND_ , default operation to combine criteria following one another.
Arity 2 (uses the next 2 criteria or combinations).

`'|'`

    

logical _OR_ , arity 2.

`'!'`

    

logical _NOT_ , arity 1.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>5

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>6

### Unlink

### Record(set) information

odoo.models.env

    

Returns the environment of the given recordset.

Type

    

`Environment`

### Operations

Recordsets are immutable, but sets of the same model can be combined using
various set operations, returning new recordsets.

  * `record in set` returns whether `record` (which must be a 1-element recordset) is present in `set`. `record not in set` is the inverse operation

  * `set1 <= set2` and `set1 < set2` return whether `set1` is a subset of `set2` (resp. strict)

  * `set1 >= set2` and `set1 > set2` return whether `set1` is a superset of `set2` (resp. strict)

  * `set1 | set2` returns the union of the two recordsets, a new recordset containing all records present in either source

  * `set1 & set2` returns the intersection of two recordsets, a new recordset containing only records present in both sources

  * `set1 - set2` returns a new recordset containing only records of `set1` which are _not_ in `set2`

Recordsets are iterable so the usual Python tools are available for
transformation ([`map()`](https://docs.python.org/3/library/functions#map
"\(disponible dans Python v3.12\)"),
[`sorted()`](https://docs.python.org/3/library/functions#sorted
"\(disponible dans Python v3.12\)"), `ifilter()`, …) however these return
either a [`list`](https://docs.python.org/3/library/stdtypes#list
"\(disponible dans Python v3.12\)") or an
[iterator](https://docs.python.org/3/glossary#term-iterator "\(disponible
dans Python v3.12\)"), removing the ability to call methods on their result,
or to use set operations.

Recordsets therefore provide the following operations returning recordsets
themselves (when possible):

#### Filter

#### Map

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>7

#### Sort

## Inheritance and extension

Konvergo ERP provides three different mechanisms to extend models in a modular way:

  * creating a new model from an existing one, adding new information to the copy but leaving the original module as-is

  * extending models defined in other modules in-place, replacing the previous version

  * delegating some of the model’s fields to records it contains

![../../../_images/inheritance_methods.png](../../../_images/inheritance_methods.png)

### Classical inheritance

When using the `_inherit` and `_name` attributes together, Konvergo ERP creates a new
model using the existing one (provided via `_inherit`) as a base. The new
model gets all the fields, methods and meta-information (defaults & al) from
its base.

    
    
    class Inheritance0(models.Model):
        _name = 'inheritance.0'
        _description = 'Inheritance Zero'
    
        name = fields.Char()
    
        def call(self):
            return self.check("model 0")
    
        def check(self, s):
            return "This is {} record {}".format(s, self.name)
    
    class Inheritance1(models.Model):
        _name = 'inheritance.1'
        _inherit = 'inheritance.0'
        _description = 'Inheritance One'
    
        def call(self):
            return self.check("model 1")
    

and using them:

    
    
    a = env['inheritance.0'].create({'name': 'A'})
    b = env['inheritance.1'].create({'name': 'B'})
    
    a.call()
    b.call()
    

will yield:

> « This is model 0 record A » « This is model 1 record B »

the second model has inherited from the first model’s `check` method and its
`name` field, but overridden the `call` method, as when using standard [Python
inheritance](https://docs.python.org/3/tutorial/classes#tut-inheritance
"\(disponible dans Python v3.12\)").

### Extension

When using `_inherit` but leaving out `_name`, the new model replaces the
existing one, essentially extending it in-place. This is useful to add new
fields or methods to existing models (created in other modules), or to
customize or reconfigure them (e.g. to change their default sort order):

    
    
    class Extension0(models.Model):
    _name = 'extension.0'
    _description = 'Extension zero'
    
    name = fields.Char(default="A")
    
    class Extension1(models.Model):
    _inherit = 'extension.0'
    
    description = fields.Char(default="Extended")
    
    
    
    record = env['extension.0'].create({})
    record.read()[0]
    

will yield:

    
    
    {'name': "A", 'description': "Extended"}
    

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>8

### Delegation

The third inheritance mechanism provides more flexibility (it can be altered
at runtime) but less power: using the `_inherits` a model _delegates_ the
lookup of any field not found on the current model to « children » models. The
delegation is performed via `Reference` fields automatically set up on the
parent model.

The main difference is in the meaning. When using Delegation, the model **has
one** instead of **is one** , turning the relationship in a composition
instead of inheritance:

    
    
    class Screen(models.Model):
        _name = 'delegation.screen'
        _description = 'Screen'
    
        size = fields.Float(string='Screen Size in inches')
    
    class Keyboard(models.Model):
        _name = 'delegation.keyboard'
        _description = 'Keyboard'
    
        layout = fields.Char(string='Layout')
    
    class Laptop(models.Model):
        _name = 'delegation.laptop'
        _description = 'Laptop'
    
        _inherits = {
            'delegation.screen': 'screen_id',
            'delegation.keyboard': 'keyboard_id',
        }
    
        name = fields.Char(string='Name')
        maker = fields.Char(string='Maker')
    
        # a Laptop has a screen
        screen_id = fields.Many2one('delegation.screen', required=True, ondelete="cascade")
        # a Laptop has a keyboard
        keyboard_id = fields.Many2one('delegation.keyboard', required=True, ondelete="cascade")
    
    
    
    record = env['delegation.laptop'].create({
        'screen_id': env['delegation.screen'].create({'size': 13.0}).id,
        'keyboard_id': env['delegation.keyboard'].create({'layout': 'QWERTY'}).id,
    })
    record.size
    record.layout
    

will result in:

    
    
    13.0
    'QWERTY'
    

and it’s possible to write directly on the delegated field:

    
    
    record.write({'size': 14.0})
    

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To parse date/datetimes coming from external sources:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">fields</span><span class="o">.</span><span class="n">Date</span><span class="o">.</span><span class="n">to_date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_context</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'date_from'</span><span class="p">))</span>
</pre></div>
</div>
</div>9 <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Strings representing dates and datetimes can be compared
between each other, however the result may not be the expected
result, as a datetime string will always be greater than a
date string, therefore this practice is <b>heavily</b>
discouraged.</p>
</div>0

### Fields Incremental Definition

A field is defined as class attribute on a model class. If the model is
extended, one can also extend the field definition by redefining a field with
the same name and same type on the subclass. In that case, the attributes of
the field are taken from the parent class and overridden by the ones given in
subclasses.

For instance, the second class below only adds a tooltip on the field `state`:

    
    
    class First(models.Model):
        _name = 'foo'
        state = fields.Selection([...], required=True)
    
    class Second(models.Model):
        _inherit = 'foo'
        state = fields.Selection(help="Blah blah blah")
    

## Error management

