Uploader for ScreenCloud
================================

ScreenCloud is an easy to use screenshot sharing tool consisting of a cross-platform client and a sharing website: [http://screencloud.net/](http://screencloud.net/)

The goal of this plugin is store (and process) your screanshots by a private endpoint.

Installation
------------

Install [URL Token Upload][current] zip in **ScreenCloud** > **Preferences** > **Online Services** > **More Services** > **Install from URL**

Or copy plugin in folder

Linux: ~/.local/share/data/screencloud/ScreenCloud/plugins/

Mac OS X: ~/Library/Application Support/screencloud/ScreenCloud/plugins

Windows: %localappdata%\screencloud\ScreenCloud\plugins

Plugin Configuration
--------------------

The plugin has a few simple configuration options

 * `Address` - URL address of your endpoint

Endpoint Configuration
----------------------

For your endpoint to interact properly with this plugin it requires the following functionality:
 * Accept `Content-Type: application/json` over `POST` request method
 * Return JSON formatted response
    * For success: `{"href": "http://example.com/<screenshot>"}`
    * For error: `{"error": "<Error> happened"}`

[current]: https://github.com/3err0/scuploader/archive/master.zip
