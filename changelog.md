# `decpys` Changelog

`decpys` follows [semantic versioning](https://semver.org/). The template for this changelog has been
adapted from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


## [Unreleased]

### Added
* Automated tests using `pytest` module
* GUI
  * define a new module `decpys.gui` to mimic functionality found in `PySide6.QtGui`
  * `decpys.gui.QIcon` (`PySide6.QtGui.QIcon` wrapper class)
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
    * set central widget
  * `decpys.widgets.qPushButton()`
    * set display using text or an icon
    * set layout
  * `decpys.widgets.qVBoxLayout()`
    * set children widgets in a list
  * `decpys.widgets.qWidget()`
    * set layout

### Changed

### Deprecated

### Removed

### Fixed

### Security



[Unreleased]: https://github.com/mbenzreba/decpys/compare/HEAD...v0.0