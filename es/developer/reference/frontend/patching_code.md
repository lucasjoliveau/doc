# Patching code

Sometimes, we need to customize the way the UI works. Many common needs are
covered by some supported API. For example, all registries are good extension
points: the field registry allows adding/removing specialized field
components, or the main component registry allows adding components that
should be displayed all the time.

However, there are situations for which it is not sufficient. In those cases,
we may need to modify an object or a class in place. To achieve that, Konvergo ERP
provides the utility function `patch`. It is mostly useful to override/update
the behavior of some other component/piece of code that one does not control.

## Description

The patch function is located in `@web/core/utils/patch`:

patch(_obj_ , _patchName_ , _patchValue_ , _options_)

    

Argumentos

    

  * **obj** (`Object()`) – object that should be patched

  * **patchName** (`string()`) – unique string describing the patch

  * **patchValue** (`Object()`) – an object mapping each key to a patchValue

  * **options** (`Object()`) – option object (see below)

The `patch` function modifies in place the `obj` object (or class) and applies
all key/value described in the `patchValue` object. This operation is
registered under the `patchName` name, so it can be unpatched later if
necessary.

Most patch operations provide access to the parent value by using the `_super`
property (see below in the examples). To do that, the `patch` method wraps
each pair key/value in a getter that dynamically binds `_super`.

The only option is `pure (boolean)`. If set to `true`, the patch operation
does not bind the `_super` property.

## Patching a simple object

Here is a simple example of how an object can be patched:

    
    
    import { patch } from "@web/core/utils/patch";
    
    const object = {
      field: "a field",
      fn() {
        // do something
      },
    };
    
    patch(object, "patch name", {
      fn() {
        // do things
      },
    });
    

When patching functions, we usually want to be able to access the `parent`
function. Since we are working with patch objects, not ES6 classes, we cannot
use the native `super` keyword. So, Konvergo ERP provides a special method to simulate
this behaviour: `this._super`:

    
    
    patch(object, "_super patch", {
      fn() {
        this._super(...arguments);
        // do other things
      },
    });
    

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p><code>this._super</code> is reassigned after each patched function is called.
This means that if you use an asynchronous function in the patch then you
cannot call <code>this._super</code> after an <code>await</code>, because it may or may not be
the function that you expect.  The correct way to do that is to keep a reference
to the initial <code>_super</code> method:</p>
<div class="highlight-javascript notranslate"><div class="highlight"><pre><span></span><span class="nx">patch</span><span class="p">(</span><span class="nx">object</span><span class="p">,</span> <span class="s2">"async _super patch"</span><span class="p">,</span> <span class="p">{</span>
  <span class="nx">async</span> <span class="nx">myAsyncFn</span><span class="p">()</span> <span class="p">{</span>
    <span class="kr">const</span> <span class="nx">_super</span> <span class="o">=</span> <span class="k">this</span><span class="p">.</span><span class="nx">_super</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="k">this</span><span class="p">);</span>
    <span class="nx">await</span> <span class="nb">Promise</span><span class="p">.</span><span class="nx">resolve</span><span class="p">();</span>
    <span class="nx">await</span> <span class="nx">_super</span><span class="p">(...</span><span class="nx">arguments</span><span class="p">);</span>
    <span class="c1">// await this._super(...arguments); // this._super is undefined.</span>
  <span class="p">},</span>
<span class="p">});</span>
</pre></div>
</div>
</div>

Getters and setters are supported too:

    
    
    patch(object, "getter/setter patch", {
      get number() {
        return this._super() / 2;
      },
      set number(value) {
        this._super(value * 2);
      },
    });
    

## Patching a javascript class

The `patch` function is designed to work with anything: object or ES6 class.

However, since javascript classes work with the prototypal inheritance, when
one wishes to patch a standard method from a class, then we actually need to
patch the `prototype`:

    
    
    class MyClass {
      static myStaticFn() {...}
      myPrototypeFn() {...}
    }
    
    // this will patch static properties!!!
    patch(MyClass, "static patch", {
      myStaticFn() {...},
    });
    
    // this is probably the usual case: patching a class method
    patch(MyClass.prototype, "prototype patch", {
      myPrototypeFn() {...},
    });
    

Also, Javascript handles the constructor in a special native way which makes
it impossible to be patched. The only workaround is to call a method in the
original constructor and patch that method instead:

    
    
    class MyClass {
      constructor() {
        this.setup();
      }
      setup() {
        this.number = 1;
      }
    }
    
    patch(MyClass.prototype, "constructor", {
      setup() {
        this._super(...arguments);
        this.doubleNumber = this.number * 2;
      },
    });
    

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>It is impossible to patch directly the <code>constructor</code> of a class!</p>
</div>

## Patching a component

Components are defined by javascript classes, so all the information above
still holds. For these reasons, Owl components should use the `setup` method,
so they can easily be patched as well (see the section on [best
practices](owl_components#frontend-owl-best-practices).

    
    
    patch(MyComponent.prototype, "my patch", {
      setup() {
        useMyHook();
      },
    });
    

## Removing a patch

The `patch` function has a counterpart, `unpatch`, also located in
`@web/core/utils/patch`.

unpatch(_obj_ , _patchName_)

    

Argumentos

    

  * **obj** (`Object()`) – object that should be unpatched

  * **patchName** (`string()`) – string describing the patch that should be removed

Removes an existing patch from an object `obj`. This is mostly useful for
testing purposes, when we patch something at the beginning of a test, and
unpatch it at the end.

    
    
    patch(object, "patch name", { ... });
    // test stuff here
    unpatch(object, "patch name");
    

