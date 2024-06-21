# Web Controllers

## Controllers

Controllers need to provide extensibility, much like `Model`, but can’t use
the same mechanism as the pre-requisites (a database with loaded modules) may
not be available yet (e.g. no database created, or no database selected).

Controllers thus provide their own extension mechanism, separate from that of
models:

Controllers are created by
[inheriting](https://docs.python.org/3/tutorial/classes#tut-inheritance
"\(disponible dans Python v3.12\)") from `Controller`. Routes are defined
through methods decorated with `route()`:

    
    
    class MyController(odoo.http.Controller):
        @route('/some_url', auth='public')
        def handler(self):
            return stuff()
    

To _override_ a controller,
[inherit](https://docs.python.org/3/tutorial/classes#tut-inheritance
"\(disponible dans Python v3.12\)") from its class and override relevant
methods, re-exposing them if necessary:

    
    
    class Extension(MyController):
        @route()
        def handler(self):
            do_before()
            return super(Extension, self).handler()
    

  * decorating with `route()` is necessary to keep the method (and route) visible: if the method is redefined without decorating, it will be « unpublished »

  * the decorators of all methods are combined, if the overriding method’s decorator has no argument all previous ones will be kept, any provided argument will override previously defined ones e.g.:
    
        class Restrict(MyController):
        @route(auth='user')
        def handler(self):
            return super(Restrict, self).handler()
    

will change `/some_url` from public authentication to user (requiring a log-
in)

## API

### Routing

### Request

The request object is automatically set on `odoo.http.request` at the start of
the request.

### Response

