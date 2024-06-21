# Web Services

The web-service module offers a common interface for all web services:

  * XML-RPC

  * JSON-RPC

Business objects can also be accessed via the distributed object mechanism.
They can all be modified via the client interface with contextual views.

Konvergo ERP is accessible through XML-RPC/JSON-RPC interfaces, for which libraries
exist in many languages.

## XML-RPC Library

The following example is a Python 3 program that interacts with an Konvergo ERP server
with the library `xmlrpc.client`:

    
    
    import xmlrpc.client
    
    root = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
    
    uid = xmlrpc.client.ServerProxy(root + 'common').login(DB, USER, PASS)
    print("Logged in as %s (uid: %d)" % (USER, uid))
    
    # Create a new note
    sock = xmlrpc.client.ServerProxy(root + 'object')
    args = {
        'color' : 8,
        'memo' : 'This is a note',
        'create_uid': uid,
    }
    note_id = sock.execute(DB, uid, PASS, 'note.note', 'create', args)
    

<div class="alert alert-dark">
<p class="alert-title">
Exercise</p><p>Add a new service to the client</p>
<p>Write a Python program able to send XML-RPC requests to a PC running
Konvergo ERP (yours, or your instructor’s). This program should display all
the sessions, and their corresponding number of seats. It should also
create a new session for one of the courses.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../reference/external_api">External API</a>: The in-depth tutorial on XML-RPC, with examples spanning multiple programming languages.</p></li>
</ul>
</div>

## JSON-RPC Library

The following example is a Python 3 program that interacts with an Konvergo ERP server
with the standard Python libraries `urllib.request` and `json`. This example
assumes the **Productivity** app (`note`) is installed:

    
    
    import json
    import random
    import urllib.request
    
    HOST = 'localhost'
    PORT = 8069
    DB = 'openacademy'
    USER = 'admin'
    PASS = 'admin'
    
    def json_rpc(url, method, params):
        data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": random.randint(0, 1000000000),
        }
        req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
            "Content-Type":"application/json",
        })
        reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
        if reply.get("error"):
            raise Exception(reply["error"])
        return reply["result"]
    
    def call(url, service, method, *args):
        return json_rpc(url, "call", {"service": service, "method": method, "args": args})
    
    # log in the given database
    url = "http://%s:%s/jsonrpc" % (HOST, PORT)
    uid = call(url, "common", "login", DB, USER, PASS)
    
    # create a new note
    args = {
        'color': 8,
        'memo': 'This is another note',
        'create_uid': uid,
    }
    note_id = call(url, "object", "execute", DB, uid, PASS, 'note.note', 'create', args)
    

Examples can be easily adapted from XML-RPC to JSON-RPC.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>There are a number of high-level APIs in various languages to access Konvergo ERP
systems without <em>explicitly</em> going through XML-RPC or JSON-RPC, such as:</p>
<ul>
<li><p><a href="https://github.com/akretion/ooor">https://github.com/akretion/ooor</a></p></li>
<li><p><a href="https://github.com/OCA/odoorpc">https://github.com/OCA/odoorpc</a></p></li>
<li><p><a href="https://github.com/nicolas-van/openerp-client-lib">https://github.com/nicolas-van/openerp-client-lib</a></p></li>
<li><p><a href="http://pythonhosted.org/Konvergo ERPRPC">http://pythonhosted.org/Konvergo ERPRPC</a></p></li>
<li><p><a href="https://github.com/abhishek-jaiswal/php-openerp-lib">https://github.com/abhishek-jaiswal/php-openerp-lib</a></p></li>
</ul>
</div>

