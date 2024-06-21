# Hooks

[Owl hooks](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md)
are a way to factorize code, even if it depends on some component lifecycle.
Most hooks provided by Owl are related to the lifecycle of a component, but
some of them (such as
[useComponent](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usecomponent))
provide a way to build specific hooks.

Using these hooks, it is possible to build many customized hooks that help
solve a specific problem, or make some common tasks easier. The rest of this
page documents the list of hooks provided by the Konvergo ERP web framework.

Name | Short Description  
---|---  
useAssets | load assets  
useAutofocus | focus automatically an element referenced by autofocus  
useBus | subscribe and unsubscribe to a bus  
usePager | Display the pager of the control panel of a view.  
usePosition | position an element relative to a target  
  
## useAssets

### Location

`@web/core/assets`

### Description

See the section on [lazy loading assets](assets#frontend-assets-lazy-
loading) for more details.

## useAutofocus

### Location

`@web/core/utils/hooks`

### Description

Focus an element referenced by a t-ref=»autofocus» in the current component as
soon as it appears in the DOM and if it was not displayed before.

    
    
    import { useAutofocus } from "@web/core/utils/hooks";
    
    class Comp {
      setup() {
        this.inputRef = useAutofocus();
      }
      static template = "Comp";
    }
    
    
    
    <t t-name="Comp" owl="1">
      <input t-ref="autofocus" type="text"/>
    </t>
    

### API

useAutofocus()

    

Devuelve

    

the element reference.

## useBus

### Location

`@web/core/utils/hooks`

### Description

Add and clear an event listener to a bus. This hook ensures that the listener
is properly cleared when the component is unmounted.

    
    
    import { useBus } from "@web/core/utils/hooks";
    
    class MyComponent {
      setup() {
        useBus(this.env.bus, "some-event", event => {
          console.log(event);
        });
      }
    }
    

### API

useBus(_bus_ , _eventName_ , _callback_)

    

Argumentos

    

  * **bus** (`EventBus()`) – the target event bus

  * **eventName** (`string()`) – the name of the event that we want to listen to

  * **callback** (`function()`) – listener callback

## usePager

### Location

`@web/search/pager_hook`

### Description

Display the [Pager](owl_components#frontend-pager) of the control panel
of a view. This hooks correctly sets `env.config` to provide the props to the
pager.

    
    
    import { usePager } from "@web/search/pager_hook";
    
    class CustomView {
      setup() {
        const state = owl.hooks.useState({
          offset: 0,
          limit: 80,
          total: 50,
        });
        usePager(() => {
          return {
            offset: this.state.offset,
            limit: this.state.limit,
            total: this.state.total,
            onUpdate: (newState) => {
              Object.assign(this.state, newState);
            },
          };
        });
      }
    }
    

### API

usePager(_getPagerProps_)

    

Argumentos

    

  * **getPagerProps** (`function()`) – function that returns the pager props.

## usePosition

### Location

`@web/core/position_hook`

### Description

Helps positioning an HTMLElement (the `popper`) relatively to another
HTMLElement (the `reference`). This hook ensures the positioning is updated
when the window is resized/scrolled.

    
    
    import { usePosition } from "@web/core/position_hook";
    
    class MyPopover extends owl.Component {
      setup() {
        // Here, the reference is the target props, which is an HTMLElement
        usePosition(this.props.target);
      }
    }
    MyPopover.template = owl.tags.xml`
      <div t-ref="popper">
        I am positioned through a wonderful hook!
      </div>
    `;
    

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>You should indicate your <code>popper</code> element using a <a href="https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref">t-ref directive</a>.</p>
</div>

### API

usePosition(_reference_[, _options_])

    

Argumentos

    

  * **reference** (`HTMLElement or ()=>HTMLElement()`) – the target HTMLElement to be positioned from

  * **options** (`Options()`) – the positioning options (see table below)

Option | Type | Description  
---|---|---  
`popper` | string | this is a [useRef reference](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref) for the element that will get positioned. Default is `"popper"`.  
`container` | HTMLElement | the container from which the popper is expected not to overflow. If overflowing occurs, other popper positions are tried until a not overflowing one is found. (default: the `<html/>` node)  
`margin` | number | added margin between popper and reference elements (default: `0`)  
`position` | Direction[-Variant] | the desired position. It is a string composed of one `Direction` and one `Variant` separated by a dash character. `Direction` could be: `top`, `bottom`, `right`, `left`. `Variant` could be: `start`, `middle`, `end`. The variant can be omitted (default variant is `middle`). Examples of valid positions: `right-end`, `top-start`, `left-middle`, `left`. (default position: `bottom`)  
`onPositioned` | (el: HTMLElement, position: PositioningSolution) => void | a callback that will be called everytime a positioning occurs (e.g. on component mounted/patched, document scroll, window resize…). Can be used i.e. for dynamic styling regarding the current position. The `PositioningSolution` is an object having the following type: `{ direction: Direction, variant: Variant, top: number, left: number }`.  
<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="highlight-javascript notranslate"><div class="highlight"><pre><span></span><span class="kr">import</span> <span class="p">{</span> <span class="nx">usePosition</span> <span class="p">}</span> <span class="nx">from</span> <span class="s2">"@web/core/position_hook"</span><span class="p">;</span>

<span class="kr">class</span> <span class="nx">DropMenu</span> <span class="kr">extends</span> <span class="nx">owl</span><span class="p">.</span><span class="nx">Component</span> <span class="p">{</span>
  <span class="nx">setup</span><span class="p">()</span> <span class="p">{</span>
    <span class="kr">const</span> <span class="nx">toggler</span> <span class="o">=</span> <span class="nx">owl</span><span class="p">.</span><span class="nx">useRef</span><span class="p">(</span><span class="s2">"toggler"</span><span class="p">);</span>
    <span class="nx">usePosition</span><span class="p">(</span>
      <span class="p">()</span> <span class="p">=&gt;</span> <span class="nx">toggler</span><span class="p">.</span><span class="nx">el</span><span class="p">,</span>
      <span class="p">{</span>
        <span class="nx">popper</span><span class="o">:</span> <span class="s2">"menu"</span><span class="p">,</span>
        <span class="nx">position</span><span class="o">:</span> <span class="s2">"right-start"</span><span class="p">,</span>
        <span class="nx">onPositioned</span><span class="o">:</span> <span class="p">(</span><span class="nx">el</span><span class="p">,</span> <span class="p">{</span> <span class="nx">direction</span><span class="p">,</span> <span class="nx">variant</span> <span class="p">})</span> <span class="p">=&gt;</span> <span class="p">{</span>
          <span class="nx">el</span><span class="p">.</span><span class="nx">classList</span><span class="p">.</span><span class="nx">add</span><span class="p">(</span><span class="sb">`dm-</span><span class="si">${</span><span class="nx">direction</span><span class="si">}</span><span class="sb">`</span><span class="p">);</span> <span class="c1">// -&gt; "dm-top" "dm-right" "dm-bottom" "dm-left"</span>
          <span class="nx">el</span><span class="p">.</span><span class="nx">style</span><span class="p">.</span><span class="nx">backgroundColor</span> <span class="o">=</span> <span class="nx">variant</span> <span class="o">===</span> <span class="s2">"middle"</span> <span class="o">?</span> <span class="s2">"red"</span> <span class="o">:</span> <span class="s2">"blue"</span><span class="p">;</span>
        <span class="p">},</span>
      <span class="p">},</span>
    <span class="p">);</span>
  <span class="p">}</span>
<span class="p">}</span>
<span class="nx">DropMenu</span><span class="p">.</span><span class="nx">template</span> <span class="o">=</span> <span class="nx">owl</span><span class="p">.</span><span class="nx">tags</span><span class="p">.</span><span class="nx">xml</span><span class="sb">`</span>
<span class="sb">  &lt;button t-ref="toggler"&gt;Toggle Menu&lt;/button&gt;</span>
<span class="sb">  &lt;div t-ref="menu"&gt;</span>
<span class="sb">    &lt;t t-slot="default"&gt;</span>
<span class="sb">      This is the menu default content.</span>
<span class="sb">    &lt;/t&gt;</span>
<span class="sb">  &lt;/div&gt;</span>
<span class="sb">`</span><span class="p">;</span>
</pre></div>
</div>
</div>

