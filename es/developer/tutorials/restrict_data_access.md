# Restrict access to data

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>This tutorial is an extension of the <a href="getting_started">Getting started</a> tutorial. Make sure you have
completed it and use the <code>estate</code> module you have built as a base for the exercises in this
tutorial. Fetch the branch <code>16.0-core</code> from the <a href="https://github.com/odoo/technical-training-solutions/tree/16.0-core">technical-training-solutions</a> repository if you
want to start from a clean base.</p>
</div>

So far we have mostly concerned ourselves with implementing useful features.
However in most business scenarios _security_ quickly becomes a concern:
currently,

  * Any employee (which is what `group_user` stands for) can create, read, update or delete properties, property types, or property tags.

  * If `estate_account` is installed then only agents allowed to interact with invoicing can confirm sales as that’s necessary to [create an invoice](getting_started/14_other_module#tutorials-getting-started-14-other-module-create).

However:

  * We do not want third parties to be able to access properties directly.

  * Not all our employees may be real-estate agents (e.g. administrative personnel, property managers, …), we don’t want non-agents to see the available properties.

  * Real-estate agents don’t need or get to decide what property types or tags are _available_.

  * Real-estate agents can have _exclusive_ properties, we do not want one agent to be able to manage another’s exclusives.

  * All real-estate agents should be able to confirm the sale of a property they can manage, but we do not want them to be able to validate or mark as paid any invoice in the system.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>

## Groups

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div> <div class="admonition-goal alert">
<p class="alert-title">
<b>Goal</b></p><p>At the end of this section,</p>
<ul>
<li><p>We can make employees <em>real-estate agents</em> or <em>real-estate managers</em>.</p></li>
<li><p>The <code>admin</code> user is a real-estate manager.</p></li>
<li><p>We have a new <em>real-estate agent</em> employee with no access to invoicing
or administration.</p></li>
</ul>
</div>

It would not be practical to attach individual security rules to employees any
time we need a change so _groups_ link security rules and users. They
correspond to roles that can be assigned to employees.

For most Konvergo ERP applications 1 a good baseline is to have _user_ and _manager_
(or administrator) roles: the manager can change the configuration of the
application and oversee the entirety of its use while the user can well, use
the application 2.

This baseline seems sufficient for us:

  * Real estate managers can configure the system (manage available types and tags) as well as oversee every property in the pipeline.

  * Real estate agents can manage the properties under their care, or properties which are not specifically under the care of any agent.

In keeping with Konvergo ERP’s data-driven nature, a group is no more than a record of
the `res.groups` model. They are normally part of a module’s [master
data](define_module_data), defined in one of the module’s data files.

As simple example [can be found
here](https://github.com/odoo/odoo/blob/532c083cbbe0ee6e7a940e2bdc9c677bd56b62fa/addons/hr/security/hr_security.xml#L9-L14).

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><ol class="arabic simple">
<li><p>Create the <code>security.xml</code> file in the appropriate folder and add it to the <code>__manifest__.py</code> file.</p></li>
<li><p>If not already, add a <code>'category'</code> field to your <code>__manifest__.py</code> with value <code>Real Estate/Brokerage</code>.</p></li>
<li><p>Add a record creating a group with the id <code>estate_group_user</code>, the name «Agent»
and the category <code>base.module_category_real_estate_brokerage</code>.</p></li>
<li><p>Below that, add a record creating a group with the id <code>estate_group_manager</code>,
the name «Manager» and the category <code>base.module_category_real_estate_brokerage</code>.
The <code>estate_group_manager</code> group needs to imply <code>estate_group_user</code>.</p></li>
</ol>
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Where does that <b>category</b> comes from ? It’s a <em>module category</em>.
Here we used the category id <code>base.module_category_real_estate_brokerage</code>
which was automatically generated by Konvergo ERP based on the <code>category</code> set in the <code>__manifest__.py</code> of the module.
You can also find here the list of
<a href="https://github.com/odoo/odoo/blob/71da80deb044852a2af6b111d695f94aad7803ac/odoo/addons/base/data/ir_module_category_data.xml">default module categories</a>
provided by Konvergo ERP.</p>
</div>
<div class="alert alert-tip">
<p class="alert-title">
Truco</p><p>Since we modified data files, remember to restart Konvergo ERP and update the
module using <code>-u estate</code>.</p>
</div>
<p>If you go to Settings ‣ Manage Users and open the
<code>admin</code> user («Mitchell Admin»), you should see a new section:</p>
<div class="figure align-default">
<img alt="../../_images/groups.png" src="../../_images/groups.png"/>
</div>
<p>Set the admin user to be a <em>Real Estate manager</em>.</p>
</div> <div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Via the web interface, create a new user with only the «real estate agent»
access. The user should not have any Invoicing or Administration access.</p>
<p>Use a private tab or window to log in with the new user (remember to set
a password), as the real-estate agent you should only see the real estate
application, and possibly the Discuss (chat) application:</p>
<div class="figure align-default">
<img alt="../../_images/agent.png" src="../../_images/agent.png"/>
</div>
</div>

## Access Rights

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found at
<a href="../reference/backend/security#reference-security-acl"><span class="std std-ref">Access Rights</span></a>.</p>
</div> <div class="admonition-goal alert">
<p class="alert-title">
<b>Goal</b></p><p>At the end of this section,</p>
<ul>
<li><p>Employees who are not at least real-estate agents will not see the
real-estate application.</p></li>
<li><p>Real-estate agents will not be able to update the property types or tags.</p></li>
</ul>
</div>

Access rights were first introduced in [Chapter 5: Security - A Brief
Introduction](getting_started/05_securityintro#tutorials-getting-
started-05-securityintro).

Access rights are a way to give users access to models _via_ groups: associate
an access right to a group, then all users with that group will have the
access.

For instance we don’t want real-estate agents to be able to modify what
property types are available, so we would not link that access to the «user»
group.

Access rights can only give access, they can’t remove it: when access is
checked, the system looks to see if _any_ access right associated with the
user (via any group) grants that access.

group | create | read | update | delete  
---|---|---|---|---  
A | X | X |  |   
B |  | X |  |   
C |  |  | X |   
  
A user with the groups A and C will be able to do anything but delete the
object while one with B and C will be able to read and update it, but not
create or delete it.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>0 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>1

Since the «demo» user was not made a real-estate agent or manager, they should
not even be able to see the real-estate application. Use a private tab or
window to check for this (the «demo» user has the password «demo»).

## Record Rules

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>3 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>4

Access rights can grant access to an entire model but often we need to be more
specific: while an agent can interact with properties in general we may not
want them to update or even see properties managed by one of their colleagues.

Record _rules_ provide that precision: they can grant or reject access to
individual records:

    
    
    <record id="rule_id" model="ir.rule">
        <field name="name">A description of the rule's role</field>
        <field name="model_id" ref="model_to_manage"/>
        <field name="perm_read" eval="False"/>
        <field name="groups" eval="[Command.link(ref('base.group_user'))]"/>
        <field name="domain_force">[
            '|', ('user_id', '=', user.id),
                 ('user_id', '=', False)
        ]</field>
    </record>
    

The [Search domains](../reference/backend/orm#reference-orm-domains) is
how access is managed: if the record passes then access is granted, otherwise
access is rejected.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>5

The rule above:

  * Only applies to the «create», «update» (write) and «delete» (unlink) operations: here we want every employee to be able to see other users” records but only the author / assignee can update a record.

  * Is [non-global](../reference/backend/security#reference-security-rules-global) so we can provide an additional rule for e.g. managers.

  * Allows the operation if the current user (`user.id`) is set (e.g. created, or is assigned) on the record, or if the record has no associated user at all.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>6 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>7

## Security Override

### Bypassing Security

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>8

If you try to mark a property as «sold» as the real estate agent, you should
get an access error:

![../../_images/error.png](../../_images/error.png)

This happens because `estate_account` tries to create an invoice during the
process, but creating an invoice requires the right to all invoice management.

We want agents to be able to confirm a sale without them having full invoicing
access, which means we need to _bypass_ the normal security checks of Konvergo ERP in
order to create an invoice _despite_ the current user not having the right to
do so.

There are two main ways to bypass existing security checks in Konvergo ERP, either
wilfully or as a side-effect:

  * The `sudo()` method will create a new recordset in «sudo mode», this ignores all access rights and record rules (although hard-coded group and user checks may still apply).

  * Performing raw SQL queries will bypass access rights and record rules as a side-effect of bypassing the ORM itself.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>We may actually be fine with some or most of these for a small business.</p>
<p>Because it’s easier for users to disable unnecessary security rules than it
is to create them from nothing, it’s better to err on the side of caution
and limit access: users can relax that access if necessary or convenient.</p>
</div>9 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>0

### Programmatically checking security

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>1

In Konvergo ERP, access rights and record rules are only checked _when performing data
access via the ORM_ e.g. creating, reading, searching, writing, or unlinking a
record via ORM methods. Other methods do _not_ necessarily check against any
sort of access rights.

In the previous section, we bypassed the record rules when creating the
invoice in `action_sold`. This bypass can be reached by any user without any
access right being checked:

  * Add a print to `action_sold` in `estate_account` before the creation of the invoice (as creating the invoice accesses the property, therefore triggers an ACL check) e.g.:
    
        print(" reached ".center(100, '='))
    

You should see `reached` in your Konvergo ERP log, followed by an access error.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>2

_Currently_ the accesses are implicitly checked by accessing data on `self` as
well as calling `super()` (which does the same and _updates_ `self`),
triggering access errors and cancelling the transaction «uncreating» our
invoice.

_However_ if this changes in the future, or we add side-effects to the method
(e.g. reporting the sale to a government agency), or bugs are introduced in
`estate`, … it would be possible for non-agents to trigger operations they
should not have access to.

Therefore when performing non-CRUD operations, or legitimately bypassing the
ORM or security, or when triggering other side-effects, it is extremely
important to perform _explicit security checks_.

Explicit security checks can be performed by:

  * Checking who the current user is (`self.env.user`) and match them against specific models or records.

  * Checking that the current user has specific groups hard-coded to allow or deny an operation (`self.env.user.has_group`).

  * Calling the `check_access_rights(operation)` method on a recordset, this verifies whether the current user has access to the model itself.

  * Calling `check_access_rule(operations)` on a non-empty recordset, this verifies that the current user is allowed to perform the operation on _every_ record of the set.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>3 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>4

## Multi-company security

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>5 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>6

For one reason or another we might need to manage our real-estate business as
multiple companies e.g. we might have largely autonomous agencies, a franchise
setup, or multiple brands (possibly from having acquired other real-estate
businesses) which remain legally or financially separate from one another.

Konvergo ERP can be used to manage multiple companies inside the same system, however
the actual handling is up to individual modules: Konvergo ERP itself provides the
tools to manage the issue of company-dependent fields and _multi-company
rules_ , which is what we’re going to concern ourselves with.

We want different agencies to be «siloed» from one another, with properties
belonging to a given agency and users (whether agents or managers) only able
to see properties linked to their agency.

As before, because this is based on non-trivial records it’s easier for a user
to relax rules than to tighten them so it makes sense to default to a
relatively stronger security model.

Multi-company rules are simply record rules based on the `company_ids` or
`company_id` fields:

  * `company_ids` is all the companies to which the current user has access

  * `company_id` is the currently active company (the one the user is currently working in / for).

Multi-company rules will _usually_ use the former i.e. check if the record is
associated with _one_ of the companies the user has access to:

    
    
    <record model="ir.rule" id="hr_appraisal_plan_comp_rule">
        <field name="name">Appraisal Plan multi-company</field>
        <field name="model_id" ref="model_hr_appraisal_plan"/>
        <field name="domain_force">[
            '|', ('company_id', '=', False),
                 ('company_id', 'in', company_ids)
        ]</field>
    </record>
    

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>7 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>8 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>The documentation related to this topic can be found in <a href="../reference/backend/security#reference-security"><span class="std std-ref">the security
reference</span></a>.</p>
<p><a href="../../contributing/development/coding_guidelines">Coding guidelines</a> document the format and
location of master data items.</p>
</div>9

## Visibility != security

<div class="admonition-goal alert">
<p class="alert-title">
<b>Goal</b></p><p>At the end of this section,</p>
<ul>
<li><p>We can make employees <em>real-estate agents</em> or <em>real-estate managers</em>.</p></li>
<li><p>The <code>admin</code> user is a real-estate manager.</p></li>
<li><p>We have a new <em>real-estate agent</em> employee with no access to invoicing
or administration.</p></li>
</ul>
</div>0

Specific Konvergo ERP models can be associated directly with groups (or companies, or
users). It is important to figure out whether this association is a _security_
or a _visibility_ feature before using it:

  * _Visibility_ features mean a user can still access the model or record otherwise, either through another part of the interface or by [performing operations remotely using RPC](../reference/external_api), things might just not be visible in the web interface in some contexts.

  * _Security_ features mean a user can not access records, fields or operations.

Here are some examples:

  * Groups on _model fields_ (in Python) are a security feature, users outside the group will not be able to retrieve the field, or even know it exists.

Example: in server actions, [only system users can see or update Python
code](https://github.com/odoo/odoo/blob/7058e338a980268df1c502b8b2860bdd8be9f727/odoo/addons/base/models/ir_actions.py#L414-L417).

  * Groups on _view elements_ (in XML) are a visibility feature, users outside the group will not be able to see the element or its content in the form but they will otherwise be able to interact with the object (including that field).

Example: [only managers have an immediate filter to see their teams”
leaves](https://github.com/odoo/odoo/blob/8e19904bcaff8300803a7b596c02ec45fcf36ae6/addons/hr_holidays/report/hr_leave_reports.xml#L16).

  * Groups on menus and actions are visibility features, the menu or action will not be shown in the interface but that doesn’t prevent directly interacting with the underlying object.

Example: [only system administrators can see the elearning settings
menu](https://github.com/odoo/odoo/blob/ff828a3e0c5386dc54e6a46fd71de9272ef3b691/addons/website_slides/views/website_slides_menu_views.xml#L64-L69).

<div class="admonition-goal alert">
<p class="alert-title">
<b>Goal</b></p><p>At the end of this section,</p>
<ul>
<li><p>We can make employees <em>real-estate agents</em> or <em>real-estate managers</em>.</p></li>
<li><p>The <code>admin</code> user is a real-estate manager.</p></li>
<li><p>We have a new <em>real-estate agent</em> employee with no access to invoicing
or administration.</p></li>
</ul>
</div>1

Despite not having access to the Property Types and Property Tags menus
anymore, agents can still access the underlying objects since they can still
select tags or a type to set on their properties.

1

    

An Konvergo ERP Application is a group of related modules covering a business area or
field, usually composed of a base module and a number of expansions on that
base to add optional or specific features, or link to other business areas.

2

    

For applications which would be used by most or every employees, the
«application user» role might be done away with and its abilities granted to
all employees directly e.g. generally all employees can submit expenses or
take time off.

