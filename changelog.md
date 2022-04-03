# `decpys` Changelog

`decpys` follows [semantic versioning](https://semver.org/). The template for this changelog has been
adapted from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


## [Unreleased]

### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security



## [0.1.0] - Released 2022-02-21

### Added
* Automated tests using `pytest` module
* Cascade
  * define a new module `decpys.cascade` to wrap Qt objects in a class that supports cascading method calls
  * `decpys.cascade.QLayoutCascader`
    * define getter of managed layout
    * define method to support setting the children of a layout 
  * `decpys.cascade.QWidgetCascader`
    * define getter of managed widget
    * define methods to support setting the widget's alignment, layout, slots, text, and icon
* GUI
  * define a new module `decpys.gui` to mimic functionality found in `PySide6.QtGui`
  * `decpys.gui.QIcon`
    * set icon file using full path
* Types
  * define a new module `decpys.types` for storing types `decpys` uses
  * `decpys.types.SignalType`
    * enumerates common Qt signals
    * define the `CLICKED` value
  * `decpys.types.onClick()`
    * returns `SignalType.CLICKED` so that top-level UI design code is as clean as possible
* Widgets
  * define a new module `decpys.widgets` to mimic functionality found in `PySide6.QtWidgets`
  * `decpys.widgets.qLabel()`
    * set alignment
    * set text
    * set layout
  * `decpys.widgets.qMainWindow()`
    * set window title
    * set central widget
  * `decpys.widgets.qPushButton()`
    * set display using text or an icon
    * set layout
    * set pairs of signals and slots
  * `decpys.widgets.qVBoxLayout()`
    * set children widgets in a list
  * `decpys.widgets.qWidget()`
    * set layout



[Unreleased]: https://github.com/mbenzreba/decpys/compare/HEAD...v0.1
[0.1.0]: https://github.com/mbenzreba/decpys/compare/HEAD...v0.0