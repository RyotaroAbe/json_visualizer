# json_visualizer

## Visualize structure of the json file.

# Example
```
[sample.json]

{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
```
## Visualise the structure
```
[In]

import json_visualizer as jv

json_path = 'sample.json'
vis = jv.visualizer(json_path)
vis.visualize()

[Out]

json
|-glossary      :       dict
 |-title        :       str
 |-GlossDiv     :       dict
  |-title       :       str
  |-GlossList   :       dict
   |-GlossEntry :       dict
    |-ID        :       str
    |-SortAs    :       str
    |-GlossTerm :       str
    |-Acronym   :       str
    |-Abbrev    :       str
    |-GlossDef  :       dict
     |-para     :       str
     |-GlossSeeAlso     :       list
       |- hoge  :       str

    |-GlossSee  :       str

```

## Show the sample value of the variable
```
[In]

json_path = 'sample.json'
vis = jv.visualizer(json_path)
vis.visualize(with_sample = True)

[Out]

json
|-glossary      :       dict
 |-title        :       str
   sample: example glossary
 |-GlossDiv     :       dict
  |-title       :       str
    sample: S
  |-GlossList   :       dict
   |-GlossEntry :       dict
    |-ID        :       str
      sample: SGML
    |-SortAs    :       str
      sample: SGML
    |-GlossTerm :       str
      sample: Standard Generalized Markup Language
    |-Acronym   :       str
      sample: SGML
    |-Abbrev    :       str
      sample: ISO 8879:1986
    |-GlossDef  :       dict
     |-para     :       str
       sample: A meta-markup language, used to create markup languages such as DocBook.
     |-GlossSeeAlso     :       list
       |- hoge  :       str
         sample: GML

    |-GlossSee  :       str
      sample: markup

```
# from command line
```
[In]

python json_visualizer.py sample.json -s

[Out]

json
|-glossary      :       dict
 |-GlossDiv     :       dict
  |-GlossList   :       dict
   |-GlossEntry :       dict
    |-GlossDef  :       dict
     |-GlossSeeAlso     :       list
       |- hoge  :       unicode
         sample: GML
     |-para     :       unicode
       sample: A meta-markup language, used to create markup languages such as DocBook.

    |-GlossSee  :       unicode
      sample: markup
    |-Acronym   :       unicode
      sample: SGML
    |-GlossTerm :       unicode
      sample: Standard Generalized Markup Language
    |-Abbrev    :       unicode
      sample: ISO 8879:1986
    |-SortAs    :       unicode
      sample: SGML
    |-ID        :       unicode
      sample: SGML


  |-title       :       unicode
    sample: S

 |-title        :       unicode
   sample: example glossary
```
