# `decpys` Changelog

`decpys` follows [semantic versioning](https://semver.org/). The template for this changelog has been
adapted from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


## [Unreleased]

### Added
* Automated tests using `pytest` module
* Core
  * `decpys.core.Alignment` (`PySide6.QtCore.Qt.AlignmentFlag` wrapper class)
    * define all basic horizontal and vertical flags
    * ability to convert from a simple integer or corresponding `PySide6` alignment flag
    * ability to convert to its corresponding `PySide6` alignment flag
* GUI
  * `decpys.gui.QIcon` (`PySide6.QtGui.QIcon` wrapper class)
    * instantiation from an icon file
    * validity check to see if an image is actually associated with the icon
* Widgets
  * `decpys.widgets.QAbstractButton`
    * basic instantiation and setters for text and icon properties
  * `decpys.widgets.QLabel` (`PySide6.QtWidgets.QLabel` wrapper class)
    * basic instantiation with or without a text label
    * get and set alignment using `decpys.core.Alignment`
    * set text
    * convenience function `qLabel()` for constructing a `Qlabel` within a declarative UI
  * `decpys.widgets.QPushButton`
    * instantiation from helper `qPushButton()`
    * set a click signal slot (event handler) using `QPushButton.onClick()`

### Changed

### Deprecated

### Removed

### Fixed

### Security



[Unreleased]: https://github.com/mbenzreba/decpys/compare/HEAD...v0.0