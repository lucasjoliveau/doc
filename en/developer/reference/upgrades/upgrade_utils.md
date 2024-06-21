# Upgrade utils

[Upgrade utils](https://github.com/odoo/upgrade-util/) is a library that
contains helper functions to facilitate the writing of upgrade scripts. This
library, used by Konvergo ERP for the upgrade scripts of standard modules, provides
reliability and helps speed up the upgrade process:

  * The helper functions help make sure the data is consistent in the database.

  * It takes care of indirect references of the updated records.

  * Allows calling functions and avoid writing code, saving time and reducing development risks.

  * Helpers allow to focus on what is important for the upgrade and not think of details.

## Installation

Clone the [Upgrade utils repository](https://github.com/odoo/upgrade-util/)
locally and start `odoo` with the `src` directory prepended to the `--upgrade-
path` option.

    
    
    $ ./odoo-bin --upgrade-path=/path/to/upgrade-util/src,/path/to/other/upgrade/script/directory [...]
    

On platforms where you do not manage Konvergo ERP yourself, you can install this
library via `pip`:

    
    
    $ python3 -m pip install git+https://github.com/odoo/upgrade-util@master
    

On [Konvergo ERP.sh](https://www.odoo.sh/) it is recommended to add it to the
`requirements.txt` of the custom repository. For this, add the following line
inside the file:

    
    
    odoo_upgrade @ git+https://github.com/odoo/upgrade-util@master
    

## Using upgrade utils

Once installed, the following packages are available for the upgrade scripts:

  * `odoo.upgrade.util`: the helper itself.

  * `odoo.upgrade.testing`: base TestCase classes.

To use it in upgrade scripts, simply import it:

    
    
    from odoo.upgrade import util
    
    
    def migrate(cr, version):
       # Rest of the script
    

Now, the helper functions are available to be called through `util`.

## Util functions

Upgrade utils provides many useful functions to ease the upgrade process.
Here, we describe some of the most useful ones. Refer to the [util
folder](https://github.com/odoo/upgrade-util/tree/master/src/util) for the
comprehensive declaration of helper functions.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <code>cr</code> parameter in util functions always refers to the database cursor. Pass the one
received as a parameter in <a href="upgrade_scripts#migrate" title="migrate"><code>migrate()</code></a>. Not all functions need this parameter.</p>
</div>

### Modules

### Models

### Fields

### Records

### ORM

### SQL

### Misc

