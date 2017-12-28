# qasi
A web app for when you need to Quickly Annotate Some Images.

## Getting started
Install requirements
```
pip install -r requirements.txt
```

Add to path:

```
PATH=$PATH:/place/where/you/downloaded/qasi
```

Fire up the qasi server: 
```
qasi --dir /my/image/directory
```

Navigate to 127.0.0.1:5000 and commence labelling!

## Todo/issues:
I hope that qasi will be helpful in some way to you. However bear in mind that I wrote qasi for myself, because I needed the ability to Quickly Annotate Some Images, nothing more, nothing less. Hence, there are a number of (quite catastrophic) limitations:

* Qasi needs to be able to create a symlink to the image directory you specify. Therefore, it will not go well for you if you attempt to use qasi on Windows.

* Only one instance of qasi should be run at a time.

* Qasi has 0% test coverage (qasi has no tests).

* Qasi is not nice to look at. Perhaps I should style the pages.
