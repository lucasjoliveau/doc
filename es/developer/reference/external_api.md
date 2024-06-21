# External API

Konvergo ERP is usually extended internally via modules, but many of its features and
all of its data are also available from the outside for external analysis or
integration with various tools. Part of the
[Models](backend/orm#reference-orm-model) API is easily available over
[XML-RPC](https://en.wikipedia.org/wiki/XML-RPC) and accessible from a variety
of languages.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Starting with PHP8, the XML-RPC extension may not be available by default.
Check out the <a href="https://www.php.net/manual/en/xmlrpc.installation.php">manual</a>
for the installation steps.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../howtos/web_services">Tutorial on web services</a></p></li>
</ul>
</div>

## Connection

### Configuration

If you already have an Konvergo ERP server installed, you can just use its parameters.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>For Konvergo ERP Online instances (&lt;domain&gt;.odoo.com), users are created without a
<em>local</em> password (as a person you are logged in via the Konvergo ERP Online
authentication system, not by the instance itself). To use XML-RPC on Konvergo ERP
Online instances, you will need to set a password on the user account you
want to use:</p>
<ul>
<li><p>Log in your instance with an administrator account.</p></li>
<li><p>Go to Settings ‣ Users &amp; Companies ‣ Users.</p></li>
<li><p>Click on the user you want to use for XML-RPC access.</p></li>
<li><p>Click on <b>Action</b> and select <b>Change Password</b>.</p></li>
<li><p>Set a <b>New Password</b> value then click <b>Change Password</b>.</p></li>
</ul>
<p>The <em>server url</em> is the instance’s domain (e.g.
<em>https://mycompany.odoo.com</em>), the <em>database name</em> is the name of the
instance (e.g. <em>mycompany</em>). The <em>username</em> is the configured user’s login
as shown by the <em>Change Password</em> screen.</p>
</div>

PythonRubyPHPJavaGo

    
    
    url = <insert server URL>
    db = <insert database name>
    username = 'admin'
    password = <insert password for your admin user (default: admin)>
    
    
    
    url = <insert server URL>
    db = <insert database name>
    username = "admin"
    password = <insert password for your admin user (default: admin)>
    
    
    
    $url = <insert server URL>;
    $db = <insert database name>;
    $username = "admin";
    $password = <insert password for your admin user (default: admin)>;
    
    
    
    final String url = <insert server URL>,
                  db = <insert database name>,
            username = "admin",
            password = <insert password for your admin user (default: admin)>;
    
    
    
    var (
        url = <insert server URL>
        db = <insert database name>
        username = "admin"
        password = <insert password for your admin user (default: admin)>
    )
    

#### API Keys

Nuevo en la versión 14.0.

Konvergo ERP has support for **api keys** and (depending on modules or settings) may
**require** these keys to perform webservice operations.

The way to use API Keys in your scripts is to simply replace your **password**
by the key. The login remains in-use. You should store the API Key as
carefully as the password as they essentially provide the same access to your
user account (although they can not be used to log-in via the interface).

In order to add a key to your account, simply go to your **Preferences** (or
**My Profile**):

![../../_images/preferences1.png](../../_images/preferences1.png)

then open the **Account Security** tab, and click **New API Key** :

![../../_images/account-security.png](../../_images/account-security.png)

Input a description for the key, **this description should be as clear and
complete as possible** : it is the only way you will have to identify your
keys later and know whether you should remove them or keep them around.

Click **Generate Key** , then copy the key provided. **Store this key
carefully** : it is equivalent to your password, and just like your password
the system will not be able to retrieve or show the key again later on. If you
lose this key, you will have to create a new one (and probably delete the one
you lost).

Once you have keys configured on your account, they will appear above the
**New API Key** button, and you will be able to delete them:

![../../_images/delete-key.png](../../_images/delete-key.png)

**A deleted API key can not be undeleted or re-set**. You will have to
generate a new key and update all the places where you used the old one.

#### Test database

To make exploration simpler, you can also ask <https://demo.odoo.com> for a
test database:

PythonRubyPHPJavaGo

    
    
    import xmlrpc.client
    info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
    url, db, username, password = info['host'], info['database'], info['user'], info['password']
    
    
    
    require "xmlrpc/client"
    info = XMLRPC::Client.new2('https://demo.odoo.com/start').call('start')
    url, db, username, password = info['host'], info['database'], info['user'], info['password']
    
    
    
    require_once('ripcord.php');
    $info = ripcord::client('https://demo.odoo.com/start')->start();
    list($url, $db, $username, $password) = array($info['host'], $info['database'], $info['user'], $info['password']);
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>These examples use the <a href="https://code.google.com/p/ripcord/">Ripcord</a>
library, which provides a simple XML-RPC API. Ripcord requires that
<a href="https://php.net/manual/en/xmlrpc.installation.php">XML-RPC support be enabled</a> in your PHP
installation.</p>
<p>Since calls are performed over
<a href="https://en.wikipedia.org/wiki/HTTP_Secure">HTTPS</a>, it also requires that
the <a href="https://php.net/manual/en/openssl.installation.php">OpenSSL extension</a> be enabled.</p>
</div>

    
    
    final XmlRpcClient client = new XmlRpcClient();
    
    final XmlRpcClientConfigImpl start_config = new XmlRpcClientConfigImpl();
    start_config.setServerURL(new URL("https://demo.odoo.com/start"));
    final Map<String, String> info = (Map<String, String>)client.execute(
        start_config, "start", emptyList());
    
    final String url = info.get("host"),
                  db = info.get("database"),
            username = info.get("user"),
            password = info.get("password");
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>These examples use the <a href="https://ws.apache.org/xmlrpc/">Apache XML-RPC library</a>.</p>
<p>The examples do not include imports as these imports couldn’t be
pasted in the code.</p>
</div>

    
    
    client, err := xmlrpc.NewClient("https://demo.odoo.com/start", nil)
    if err != nil {
        log.Fatal(err)
    }
    info := map[string]string{}
    client.Call("start", nil, &info)
    url = info["host"].(string)
    db = info["database"].(string)
    username = info["user"].(string)
    password = info["password"].(string)
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>These examples use the <a href="https://github.com/kolo/xmlrpc">github.com/kolo/xmlrpc library</a>.</p>
<p>The examples do not include imports as these imports couldn’t be
pasted in the code.</p>
</div>

### Logging in

Konvergo ERP requires users of the API to be authenticated before they can query most
data.

The `xmlrpc/2/common` endpoint provides meta-calls which don’t require
authentication, such as the authentication itself or fetching version
information. To verify if the connection information is correct before trying
to authenticate, the simplest call is to ask for the server’s version. The
authentication itself is done through the `authenticate` function and returns
a user identifier (`uid`) used in authenticated calls instead of the login.

PythonRubyPHPJavaGo

    
    
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    common.version()
    
    
    
    common = XMLRPC::Client.new2("#{url}/xmlrpc/2/common")
    common.call('version')
    
    
    
    $common = ripcord::client("$url/xmlrpc/2/common");
    $common->version();
    
    
    
    final XmlRpcClientConfigImpl common_config = new XmlRpcClientConfigImpl();
    common_config.setServerURL(new URL(String.format("%s/xmlrpc/2/common", url)));
    client.execute(common_config, "version", emptyList());
    
    
    
    client, err := xmlrpc.NewClient(fmt.Sprintf("%s/xmlrpc/2/common", url), nil)
    if err != nil {
        log.Fatal(err)
    }
    common := map[string]any{}
    if err := client.Call("version", nil, &common); err != nil {
        log.Fatal(err)
    }
    

Result:

    
    
    {
        "server_version": "13.0",
        "server_version_info": [13, 0, 0, "final", 0],
        "server_serie": "13.0",
        "protocol_version": 1,
    }
    

PythonRubyPHPJavaGo

    
    
    uid = common.authenticate(db, username, password, {})
    
    
    
    uid = common.call('authenticate', db, username, password, {})
    
    
    
    $uid = $common->authenticate($db, $username, $password, array());
    
    
    
    int uid = (int)client.execute(common_config, "authenticate", asList(db, username, password, emptyMap()));
    
    
    
    var uid int64
    if err := client.Call("authenticate", []any{
        db, username, password,
        map[string]any{},
    }, &uid); err != nil {
        log.Fatal(err)
    }
    

## Calling methods

The second endpoint is `xmlrpc/2/object`. It is used to call methods of odoo
models via the `execute_kw` RPC function.

Each call to `execute_kw` takes the following parameters:

  * the database to use, a string

  * the user id (retrieved through `authenticate`), an integer

  * the user’s password, a string

  * the model name, a string

  * the method name, a string

  * an array/list of parameters passed by position

  * a mapping/dict of parameters to pass by keyword (optional)

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>For instance, to see if we can read the <code>res.partner</code> model, we can call
<code>check_access_rights</code> with <code>operation</code> passed by position and
<code>raise_exception</code> passed by keyword (in order to get a true/false result
rather than true/error):</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-4-UHl0aG9u" aria-selected="true" class="sphinx-tabs-tab code-tab group-tab" id="tab-4-UHl0aG9u" name="UHl0aG9u" role="tab" tabindex="0">Python</button><button aria-controls="panel-4-UnVieQ==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-4-UnVieQ==" name="UnVieQ==" role="tab" tabindex="-1">Ruby</button><button aria-controls="panel-4-UEhQ" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-4-UEhQ" name="UEhQ" role="tab" tabindex="-1">PHP</button><button aria-controls="panel-4-SmF2YQ==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-4-SmF2YQ==" name="SmF2YQ==" role="tab" tabindex="-1">Java</button><button aria-controls="panel-4-R28=" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-4-R28=" name="R28=" role="tab" tabindex="-1">Go</button></div><div aria-labelledby="tab-4-UHl0aG9u" class="sphinx-tabs-panel code-tab group-tab" id="panel-4-UHl0aG9u" name="UHl0aG9u" role="tabpanel" tabindex="0"><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="n">models</span> <span class="o">=</span> <span class="n">xmlrpc</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">ServerProxy</span><span class="p">(</span><span class="s1">'</span><span class="si">{}</span><span class="s1">/xmlrpc/2/object'</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">url</span><span class="p">))</span>
<span class="n">models</span><span class="o">.</span><span class="n">execute_kw</span><span class="p">(</span><span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'check_access_rights'</span><span class="p">,</span> <span class="p">[</span><span class="s1">'read'</span><span class="p">],</span> <span class="p">{</span><span class="s1">'raise_exception'</span><span class="p">:</span> <span class="kc">False</span><span class="p">})</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-4-UnVieQ==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-4-UnVieQ==" name="UnVieQ==" role="tabpanel" tabindex="0"><div class="highlight-ruby notranslate"><div class="highlight"><pre><span></span><span class="n">models</span> <span class="o">=</span> <span class="no">XMLRPC</span><span class="o">::</span><span class="no">Client</span><span class="o">.</span><span class="n">new2</span><span class="p">(</span><span class="s2">"</span><span class="si">#{</span><span class="n">url</span><span class="si">}</span><span class="s2">/xmlrpc/2/object"</span><span class="p">)</span><span class="o">.</span><span class="n">proxy</span>
<span class="n">models</span><span class="o">.</span><span class="n">execute_kw</span><span class="p">(</span><span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'check_access_rights'</span><span class="p">,</span> <span class="o">[</span><span class="s1">'read'</span><span class="o">]</span><span class="p">,</span> <span class="p">{</span><span class="ss">raise_exception</span><span class="p">:</span> <span class="kp">false</span><span class="p">})</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-4-UEhQ" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-4-UEhQ" name="UEhQ" role="tabpanel" tabindex="0"><div class="highlight-php notranslate"><div class="highlight"><pre><span></span><span class="nv">$models</span> <span class="o">=</span> <span class="nx">ripcord</span><span class="o">::</span><span class="na">client</span><span class="p">(</span><span class="s2">"</span><span class="si">$url</span><span class="s2">/xmlrpc/2/object"</span><span class="p">);</span>
<span class="nv">$models</span><span class="o">-&gt;</span><span class="na">execute_kw</span><span class="p">(</span><span class="nv">$db</span><span class="p">,</span> <span class="nv">$uid</span><span class="p">,</span> <span class="nv">$password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'check_access_rights'</span><span class="p">,</span> <span class="k">array</span><span class="p">(</span><span class="s1">'read'</span><span class="p">),</span> <span class="k">array</span><span class="p">(</span><span class="s1">'raise_exception'</span> <span class="o">=&gt;</span> <span class="k">false</span><span class="p">));</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-4-SmF2YQ==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-4-SmF2YQ==" name="SmF2YQ==" role="tabpanel" tabindex="0"><div class="highlight-java notranslate"><div class="highlight"><pre><span></span><span class="kd">final</span> <span class="n">XmlRpcClient</span> <span class="n">models</span> <span class="o">=</span> <span class="k">new</span> <span class="n">XmlRpcClient</span><span class="p">()</span> <span class="p">{{</span>
    <span class="n">setConfig</span><span class="p">(</span><span class="k">new</span> <span class="n">XmlRpcClientConfigImpl</span><span class="p">()</span> <span class="p">{{</span>
        <span class="n">setServerURL</span><span class="p">(</span><span class="k">new</span> <span class="n">URL</span><span class="p">(</span><span class="n">String</span><span class="p">.</span><span class="na">format</span><span class="p">(</span><span class="s">"%s/xmlrpc/2/object"</span><span class="p">,</span> <span class="n">url</span><span class="p">)));</span>
    <span class="p">}});</span>
<span class="p">}};</span>
<span class="n">models</span><span class="p">.</span><span class="na">execute</span><span class="p">(</span><span class="s">"execute_kw"</span><span class="p">,</span> <span class="n">asList</span><span class="p">(</span>
    <span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span>
    <span class="s">"res.partner"</span><span class="p">,</span> <span class="s">"check_access_rights"</span><span class="p">,</span>
    <span class="n">asList</span><span class="p">(</span><span class="s">"read"</span><span class="p">),</span>
    <span class="k">new</span> <span class="n">HashMap</span><span class="p">()</span> <span class="p">{{</span> <span class="n">put</span><span class="p">(</span><span class="s">"raise_exception"</span><span class="p">,</span> <span class="kc">false</span><span class="p">);</span> <span class="p">}}</span>
<span class="p">));</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-4-R28=" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-4-R28=" name="R28=" role="tabpanel" tabindex="0"><div class="highlight-go notranslate"><div class="highlight"><pre><span></span><span class="nx">models</span><span class="p">,</span> <span class="nx">err</span> <span class="o">:=</span> <span class="nx">xmlrpc</span><span class="p">.</span><span class="nx">NewClient</span><span class="p">(</span><span class="nx">fmt</span><span class="p">.</span><span class="nx">Sprintf</span><span class="p">(</span><span class="s">"%s/xmlrpc/2/object"</span><span class="p">,</span> <span class="nx">url</span><span class="p">),</span> <span class="kc">nil</span><span class="p">)</span>
<span class="k">if</span> <span class="nx">err</span> <span class="o">!=</span> <span class="kc">nil</span> <span class="p">{</span>
    <span class="nx">log</span><span class="p">.</span><span class="nx">Fatal</span><span class="p">(</span><span class="nx">err</span><span class="p">)</span>
<span class="p">}</span>
<span class="kd">var</span> <span class="nx">result</span> <span class="kt">bool</span>
<span class="k">if</span> <span class="nx">err</span> <span class="o">:=</span> <span class="nx">models</span><span class="p">.</span><span class="nx">Call</span><span class="p">(</span><span class="s">"execute_kw"</span><span class="p">,</span> <span class="p">[]</span><span class="nx">any</span><span class="p">{</span>
    <span class="nx">db</span><span class="p">,</span> <span class="nx">uid</span><span class="p">,</span> <span class="nx">password</span><span class="p">,</span>
    <span class="s">"res.partner"</span><span class="p">,</span> <span class="s">"check_access_rights"</span><span class="p">,</span>
    <span class="p">[]</span><span class="kt">string</span><span class="p">{</span><span class="s">"read"</span><span class="p">},</span>
    <span class="kd">map</span><span class="p">[</span><span class="kt">string</span><span class="p">]</span><span class="kt">bool</span><span class="p">{</span><span class="s">"raise_exception"</span><span class="p">:</span> <span class="kc">false</span><span class="p">},</span>
<span class="p">},</span> <span class="o">&amp;</span><span class="nx">result</span><span class="p">);</span> <span class="nx">err</span> <span class="o">!=</span> <span class="kc">nil</span> <span class="p">{</span>
    <span class="nx">log</span><span class="p">.</span><span class="nx">Fatal</span><span class="p">(</span><span class="nx">err</span><span class="p">)</span>
<span class="p">}</span>
</pre></div>
</div>
</div></div>
<p>Result:</p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="kc">true</span>
</pre></div>
</div>
</div>

### List records

Records can be listed and filtered via `search()`.

`search()` takes a mandatory [domain](backend/orm#reference-orm-domains)
filter (possibly empty), and returns the database identifiers of all records
matching the filter.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To list customer companies, for instance:</p>
<div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-5-UHl0aG9u" aria-selected="true" class="sphinx-tabs-tab code-tab group-tab" id="tab-5-UHl0aG9u" name="UHl0aG9u" role="tab" tabindex="0">Python</button><button aria-controls="panel-5-UnVieQ==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-5-UnVieQ==" name="UnVieQ==" role="tab" tabindex="-1">Ruby</button><button aria-controls="panel-5-UEhQ" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-5-UEhQ" name="UEhQ" role="tab" tabindex="-1">PHP</button><button aria-controls="panel-5-SmF2YQ==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-5-SmF2YQ==" name="SmF2YQ==" role="tab" tabindex="-1">Java</button><button aria-controls="panel-5-R28=" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-5-R28=" name="R28=" role="tab" tabindex="-1">Go</button></div><div aria-labelledby="tab-5-UHl0aG9u" class="sphinx-tabs-panel code-tab group-tab" id="panel-5-UHl0aG9u" name="UHl0aG9u" role="tabpanel" tabindex="0"><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="n">models</span><span class="o">.</span><span class="n">execute_kw</span><span class="p">(</span><span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'search'</span><span class="p">,</span> <span class="p">[[[</span><span class="s1">'is_company'</span><span class="p">,</span> <span class="s1">'='</span><span class="p">,</span> <span class="kc">True</span><span class="p">]]])</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-5-UnVieQ==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-5-UnVieQ==" name="UnVieQ==" role="tabpanel" tabindex="0"><div class="highlight-ruby notranslate"><div class="highlight"><pre><span></span><span class="n">models</span><span class="o">.</span><span class="n">execute_kw</span><span class="p">(</span><span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'search'</span><span class="p">,</span> <span class="o">[[[</span><span class="s1">'is_company'</span><span class="p">,</span> <span class="s1">'='</span><span class="p">,</span> <span class="kp">true</span><span class="o">]]]</span><span class="p">)</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-5-UEhQ" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-5-UEhQ" name="UEhQ" role="tabpanel" tabindex="0"><div class="highlight-php notranslate"><div class="highlight"><pre><span></span><span class="nv">$models</span><span class="o">-&gt;</span><span class="na">execute_kw</span><span class="p">(</span><span class="nv">$db</span><span class="p">,</span> <span class="nv">$uid</span><span class="p">,</span> <span class="nv">$password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'search'</span><span class="p">,</span> <span class="k">array</span><span class="p">(</span><span class="k">array</span><span class="p">(</span><span class="k">array</span><span class="p">(</span><span class="s1">'is_company'</span><span class="p">,</span> <span class="s1">'='</span><span class="p">,</span> <span class="k">true</span><span class="p">))));</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-5-SmF2YQ==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-5-SmF2YQ==" name="SmF2YQ==" role="tabpanel" tabindex="0"><div class="highlight-java notranslate"><div class="highlight"><pre><span></span><span class="n">asList</span><span class="p">((</span><span class="n">Object</span><span class="o">[]</span><span class="p">)</span><span class="n">models</span><span class="p">.</span><span class="na">execute</span><span class="p">(</span><span class="s">"execute_kw"</span><span class="p">,</span> <span class="n">asList</span><span class="p">(</span>
    <span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span>
    <span class="s">"res.partner"</span><span class="p">,</span> <span class="s">"search"</span><span class="p">,</span>
    <span class="n">asList</span><span class="p">(</span><span class="n">asList</span><span class="p">(</span>
        <span class="n">asList</span><span class="p">(</span><span class="s">"is_company"</span><span class="p">,</span> <span class="s">"="</span><span class="p">,</span> <span class="kc">true</span><span class="p">)))</span>
<span class="p">)));</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-5-R28=" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-5-R28=" name="R28=" role="tabpanel" tabindex="0"><div class="highlight-go notranslate"><div class="highlight"><pre><span></span><span class="kd">var</span> <span class="nx">records</span> <span class="p">[]</span><span class="kt">int64</span>
<span class="k">if</span> <span class="nx">err</span> <span class="o">:=</span> <span class="nx">models</span><span class="p">.</span><span class="nx">Call</span><span class="p">(</span><span class="s">"execute_kw"</span><span class="p">,</span> <span class="p">[]</span><span class="nx">any</span><span class="p">{</span>
    <span class="nx">db</span><span class="p">,</span> <span class="nx">uid</span><span class="p">,</span> <span class="nx">password</span><span class="p">,</span>
    <span class="s">"res.partner"</span><span class="p">,</span> <span class="s">"search"</span><span class="p">,</span>
    <span class="p">[]</span><span class="nx">any</span><span class="p">{[]</span><span class="nx">any</span><span class="p">{</span>
        <span class="p">[]</span><span class="nx">any</span><span class="p">{</span><span class="s">"is_company"</span><span class="p">,</span> <span class="s">"="</span><span class="p">,</span> <span class="kc">true</span><span class="p">},</span>
    <span class="p">}},</span>
<span class="p">},</span> <span class="o">&amp;</span><span class="nx">records</span><span class="p">);</span> <span class="nx">err</span> <span class="o">!=</span> <span class="kc">nil</span> <span class="p">{</span>
    <span class="nx">log</span><span class="p">.</span><span class="nx">Fatal</span><span class="p">(</span><span class="nx">err</span><span class="p">)</span>
<span class="p">}</span>
</pre></div>
</div>
</div></div>
<p>Result:</p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">[</span><span class="mi">7</span><span class="p">,</span> <span class="mi">18</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">14</span><span class="p">,</span> <span class="mi">17</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">26</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">13</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">22</span><span class="p">,</span> <span class="mi">29</span><span class="p">,</span> <span class="mi">15</span><span class="p">,</span> <span class="mi">23</span><span class="p">,</span> <span class="mi">28</span><span class="p">,</span> <span class="mi">74</span><span class="p">]</span>
</pre></div>
</div>
</div>

#### Pagination

By default a search will return the ids of all records matching the condition,
which may be a huge number. `offset` and `limit` parameters are available to
only retrieve a subset of all matched records.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-6-UHl0aG9u" aria-selected="true" class="sphinx-tabs-tab code-tab group-tab" id="tab-6-UHl0aG9u" name="UHl0aG9u" role="tab" tabindex="0">Python</button><button aria-controls="panel-6-UnVieQ==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-6-UnVieQ==" name="UnVieQ==" role="tab" tabindex="-1">Ruby</button><button aria-controls="panel-6-UEhQ" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-6-UEhQ" name="UEhQ" role="tab" tabindex="-1">PHP</button><button aria-controls="panel-6-SmF2YQ==" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-6-SmF2YQ==" name="SmF2YQ==" role="tab" tabindex="-1">Java</button><button aria-controls="panel-6-R28=" aria-selected="false" class="sphinx-tabs-tab code-tab group-tab" id="tab-6-R28=" name="R28=" role="tab" tabindex="-1">Go</button></div><div aria-labelledby="tab-6-UHl0aG9u" class="sphinx-tabs-panel code-tab group-tab" id="panel-6-UHl0aG9u" name="UHl0aG9u" role="tabpanel" tabindex="0"><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="n">models</span><span class="o">.</span><span class="n">execute_kw</span><span class="p">(</span><span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'search'</span><span class="p">,</span> <span class="p">[[[</span><span class="s1">'is_company'</span><span class="p">,</span> <span class="s1">'='</span><span class="p">,</span> <span class="kc">True</span><span class="p">]]],</span> <span class="p">{</span><span class="s1">'offset'</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span> <span class="s1">'limit'</span><span class="p">:</span> <span class="mi">5</span><span class="p">})</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-6-UnVieQ==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-6-UnVieQ==" name="UnVieQ==" role="tabpanel" tabindex="0"><div class="highlight-ruby notranslate"><div class="highlight"><pre><span></span><span class="n">models</span><span class="o">.</span><span class="n">execute_kw</span><span class="p">(</span><span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'search'</span><span class="p">,</span> <span class="o">[[[</span><span class="s1">'is_company'</span><span class="p">,</span> <span class="s1">'='</span><span class="p">,</span> <span class="kp">true</span><span class="o">]]]</span><span class="p">,</span> <span class="p">{</span><span class="ss">offset</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span> <span class="ss">limit</span><span class="p">:</span> <span class="mi">5</span><span class="p">})</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-6-UEhQ" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-6-UEhQ" name="UEhQ" role="tabpanel" tabindex="0"><div class="highlight-php notranslate"><div class="highlight"><pre><span></span><span class="nv">$models</span><span class="o">-&gt;</span><span class="na">execute_kw</span><span class="p">(</span><span class="nv">$db</span><span class="p">,</span> <span class="nv">$uid</span><span class="p">,</span> <span class="nv">$password</span><span class="p">,</span> <span class="s1">'res.partner'</span><span class="p">,</span> <span class="s1">'search'</span><span class="p">,</span> <span class="k">array</span><span class="p">(</span><span class="k">array</span><span class="p">(</span><span class="k">array</span><span class="p">(</span><span class="s1">'is_company'</span><span class="p">,</span> <span class="s1">'='</span><span class="p">,</span> <span class="k">true</span><span class="p">))),</span> <span class="k">array</span><span class="p">(</span><span class="s1">'offset'</span><span class="o">=&gt;</span><span class="mi">10</span><span class="p">,</span> <span class="s1">'limit'</span><span class="o">=&gt;</span><span class="mi">5</span><span class="p">));</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-6-SmF2YQ==" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-6-SmF2YQ==" name="SmF2YQ==" role="tabpanel" tabindex="0"><div class="highlight-java notranslate"><div class="highlight"><pre><span></span><span class="n">asList</span><span class="p">((</span><span class="n">Object</span><span class="o">[]</span><span class="p">)</span><span class="n">models</span><span class="p">.</span><span class="na">execute</span><span class="p">(</span><span class="s">"execute_kw"</span><span class="p">,</span> <span class="n">asList</span><span class="p">(</span>
    <span class="n">db</span><span class="p">,</span> <span class="n">uid</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span>
    <span class="s">"res.partner"</span><span class="p">,</span> <span class="s">"search"</span><span class="p">,</span>
    <span class="n">asList</span><span class="p">(</span><span class="n">asList</span><span class="p">(</span>
        <span class="n">asList</span><span class="p">(</span><span class="s">"is_company"</span><span class="p">,</span> <span class="s">"="</span><span class="p">,</span> <span class="kc">true</span><span class="p">))),</span>
    <span class="k">new</span> <span class="n">HashMap</span><span class="p">()</span> <span class="p">{{</span> <span class="n">put</span><span class="p">(</span><span class="s">"offset"</span><span class="p">,</span> <span class="mi">10</span><span class="p">);</span> <span class="n">put</span><span class="p">(</span><span class="s">"limit"</span><span class="p">,</span> <span class="mi">5</span><span class="p">);</span> <span class="p">}}</span>
<span class="p">)));</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-6-R28=" class="sphinx-tabs-panel code-tab group-tab" hidden="true" id="panel-6-R28=" name="R28=" role="tabpanel" tabindex="0"><div class="highlight-go notranslate"><div class="highlight"><pre><span></span><span class="kd">var</span> <span class="nx">records</span> <span class="p">[]</span><span class="kt">int64</span>
<span class="k">if</span> <span class="nx">err</span> <span class="o">:=</span> <span class="nx">models</span><span class="p">.</span><span class="nx">Call</span><span class="p">(</span><span class="s">"execute_kw"</span><span class="p">,</span> <span class="p">[]</span><span class="nx">any</span><span class="p">{</span>
    <span class="nx">db</span><span class="p">,</span> <span class="nx">uid</span><span class="p">,</span> <span class="nx">password</span><span class="p">,</span>
    <span class="s">"res.partner"</span><span class="p">,</span> <span class="s">"search"</span><span class="p">,</span>
    <span class="p">[]</span><span class="nx">any</span><span class="p">{[]</span><span class="nx">any</span><span class="p">{</span>
        <span class="p">[]</span><span class="nx">any</span><span class="p">{</span><span class="s">"is_company"</span><span class="p">,</span> <span class="s">"="</span><span class="p">,</span> <span class="kc">true</span><span class="p">},</span>
    <span class="p">}},</span>
    <span class="kd">map</span><span class="p">[</span><span class="kt">string</span><span class="p">]</span><span class="kt">int64</span><span class="p">{</span><span class="s">"offset"</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span> <span class="s">"limit"</span><span class="p">:</span>  <span class="mi">5</span><span class="p">},</span>
<span class="p">},</span> <span class="o">&amp;</span><span class="nx">records</span><span class="p">);</span> <span class="nx">err</span> <span class="o">!=</span> <span class="kc">nil</span> <span class="p">{</span>
    <span class="nx">log</span><span class="p">.</span><span class="nx">Fatal</span><span class="p">(</span><span class="nx">err</span><span class="p">)</span>
<span class="p">}</span>
</pre></div>
</div>
</div></div>
<p>Result:</p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">[</span><span class="mi">13</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">22</span><span class="p">,</span> <span class="mi">29</span><span class="p">]</span>
</pre></div>
</div>
</div>

### Count records

Rather than retrieve a possibly gigantic list of records and count them,
`search_count()` can be used to retrieve only the number of records matching
the query. It takes the same [domain](backend/orm#reference-orm-domains)
filter as `search()` and no other parameter.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>0 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>1

### Read records

Record data are accessible via the `read()` method, which takes a list of ids
(as returned by `search()`), and optionally a list of fields to fetch. By
default, it fetches all the fields the current user can read, which tends to
be a huge amount.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>2 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>3

### List record fields

`fields_get()` can be used to inspect a model’s fields and check which ones
seem to be of interest.

Because it returns a large amount of meta-information (it is also used by
client programs) it should be filtered before printing, the most interesting
items for a human user are `string` (the field’s label), `help` (a help text
if available) and `type` (to know which values to expect, or to send when
updating a record).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>4

### Search and read

Because it is a very common task, Konvergo ERP provides a `search_read()` shortcut
which, as its name suggests, is equivalent to a `search()` followed by a
`read()`, but avoids having to perform two requests and keep ids around.

Its arguments are similar to `search()`”s, but it can also take a list of
`fields` (like `read()`, if that list is not provided it will fetch all fields
of matched records).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>5

### Create records

Records of a model are created using `create()`. The method creates a single
record and returns its database identifier.

`create()` takes a mapping of fields to values, used to initialize the record.
For any field which has a default value and is not set through the mapping
argument, the default value will be used.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>6 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>7

### Update records

Records can be updated using `write()`. It takes a list of records to update
and a mapping of updated fields to values similar to `create()`.

Multiple records can be updated simultaneously, but they will all get the same
values for the fields being set. It is not possible to perform «computed»
updates (where the value being set depends on an existing value of a record).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>8

### Delete records

Records can be deleted in bulk by providing their ids to `unlink()`.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Access to data via the external API is only available on <em>Custom</em> Konvergo ERP pricing plans. Access to
the external API is not available on <em>One App Free</em> or <em>Standard</em> plans. For more information
visit the <a href="https://www.odoo.com/pricing-plan">Konvergo ERP pricing page</a> or reach out to your Customer
Success Manager.</p>
</div>9

### Inspection and introspection

While we previously used `fields_get()` to query a model and have been using
an arbitrary model from the start, Konvergo ERP stores most model metadata inside a
few meta-models which allow both querying the system and altering models and
fields (with some limitations) on the fly over XML-RPC.

#### `ir.model`

Provides information about Konvergo ERP models via its various fields.

`name`

    

a human-readable description of the model

`model`

    

the name of each model in the system

`state`

    

whether the model was generated in Python code (`base`) or by creating an
`ir.model` record (`manual`)

`field_id`

    

list of the model’s fields through a `One2many` to ir.model.fields

`view_ids`

    

`One2many` to the [Views](backend/views#reference-views) defined for the
model

`access_ids`

    

`One2many` relation to the [Access Rights](backend/security#reference-
security-acl) set on the model

`ir.model` can be used to

  * Query the system for installed models (as a precondition to operations on the model or to explore the system’s content).

  * Get information about a specific model (generally by listing the fields associated with it).

  * Create new models dynamically over RPC.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../howtos/web_services">Tutorial on web services</a></p></li>
</ul>
</div>0 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../howtos/web_services">Tutorial on web services</a></p></li>
</ul>
</div>1

#### `ir.model.fields`

Provides information about the fields of Konvergo ERP models and allows adding custom
fields without using Python code.

`model_id`

    

`Many2one` to ir.model to which the field belongs

`name`

    

the field’s technical name (used in `read` or `write`)

`field_description`

    

the field’s user-readable label (e.g. `string` in `fields_get`)

`ttype`

    

the [type](backend/orm#reference-orm-fields) of field to create

`state`

    

whether the field was created via Python code (`base`) or via
`ir.model.fields` (`manual`)

`required`, `readonly`, `translate`

    

enables the corresponding flag on the field

`groups`

    

[field-level access control](backend/security#reference-security-fields),
a `Many2many` to `res.groups`

`selection`, `size`, `on_delete`, `relation`, `relation_field`, `domain`

    

type-specific properties and customizations, see [the fields
documentation](backend/orm#reference-orm-fields) for details

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../howtos/web_services">Tutorial on web services</a></p></li>
</ul>
</div>2 <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../howtos/web_services">Tutorial on web services</a></p></li>
</ul>
</div>3

