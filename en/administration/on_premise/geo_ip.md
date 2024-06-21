# Geo IP

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This documentation only applies to On-premise databases.</p>
</div>

## Installation

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Please note that the installation depends on your computer’s operating system and distribution.
We will assume that a Linux operating system is being used.</p>
</div>

  1. Install [geoip2](https://pypi.org/project/geoip2/) Python library
    
    
        pip install geoip2
    

  2. Download the [GeoLite2 City database](https://dev.maxmind.com/geoip/geoip2/geolite2/). You should end up with a file called `GeoLite2-City.mmdb`

  3. Move the file to the folder `/usr/share/GeoIP/`
    
    
        mv ~/Downloads/GeoLite2-City.mmdb /usr/share/GeoIP/
    

  4. Restart the server

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If you can’t/don’t want to locate the geoip database in <code>/usr/share/GeoIP/</code>, you can use the
<code>--geoip-db</code> option of the Konvergo ERP command line interface. This option takes the absolute path to
the GeoIP database file and uses it as the GeoIP database. For example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>./odoo-bin --geoip-db<span class="o">=</span> ~/Downloads/GeoLite2-City.mmdb
</pre></div>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../developer/reference/cli">CLI documentation</a>.</p></li>
</ul>
</div>
</div> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p><code>GeoIP</code> Python library can also be used. However this version is discontinued since January
1.    See <a href="https://support.maxmind.com/geolite-legacy-discontinuation-notice/">GeoLite Legacy databases are now discontinued</a></p>
</div>

## How to test GeoIP geolocation in your Konvergo ERP website

  1. Go to your website. Open the web page that you want to test `GeoIP`.

  2. Choose Customize ‣ HTML/CSS/JS Editor.

  3. Add the following piece of XML in the page :

    
    
    <h1 class="text-center" t-esc="request.session.get('geoip')"/>
    

You should end up with a dictionary indicating the location of the IP address.

![../../_images/on-premise_geo-ip-installation01.png](../../_images/on-
premise_geo-ip-installation01.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the curly braces are empty <code>{}</code>, it can be for any of the following reasons :</p>
<ul>
<li><p>The browsing IP address is the localhost (<code>127.0.0.1</code>) or a local area network one
(<code>192.168.*.*</code>)</p></li>
<li><p>If a reversed proxy is used, make sure to configure it correctly. See <a href="../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode"><code>proxy mode</code></a></p></li>
<li><p><code>geoip2</code> is not installed or the GeoIP database file wasn’t found</p></li>
<li><p>The GeoIP database was unable to resolve the given IP address</p></li>
</ul>
</div>

