django-bootstrap-static-files
=============================

First, add to your project by adding...

`    'bootstrap_static_files',`

to your settings.INSTALLED\_APPS variable. 

In your template, first load the tags

`{% load bootstrap_tags %}`

Then you can get the (entire) bootstrap js/css/less tags by typing
(js)
`{% get_bootstrap_js_tags %}`
(css)
`{% get_bootstrap_css_tags %}`
(less)
`{% get_bootstrap_less_tags %}`

If you want to reference them manually, you can find them in
`{{ STATIC_URL }}bootstrap/{js,css,less}/bootstrap.{js,css,less}`

Good luck and have fun!
