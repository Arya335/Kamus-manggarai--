import cgi
import cgitb; cgitb.enable()  
import simplejson as json

print "Content-type: text/html"

print """
<html>
<head><title>Kamus Indonesia - Manggarai</title></head>
<body>
  <h1>Kamus Indonesia - Manggarai </h1>
  <form method="post" action="index.cgi">
    <label>Bahasa Indonesia</label><br/>
    <input type="text" name="kata"/></p>
    <input type="submit" name="submit" value="Terjemahkan"/></p>
  </form>
  Manggarai:<br/>  
"""

form = cgi.FieldStorage()
cari_kata = form.getvalue("kata")

location_database = open('dataKamus.json', 'r')
bhs_mgr = json.load(location_database)

if cari_kata:   
   for bhs_indonesia in cari_kata.split(' '): 
    for arti_kata in bhs_mgr:   
     if arti_kata["indonesia"] == bhs_indonesia.replace(' ',''):
         hasil = arti_kata['inggris'] 
        break
    else:
        hasil = "<toe manga hasil>"   
               
    print """
    <input type="text" name="hasil" value="%s"/>
    </body>
    </html>
    """ % cgi.escape(hasil)
