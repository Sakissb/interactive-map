# This file contains the configuration settings for building the Android application using Buildozer.

[app]
title = Interactive Map App
package.name = interactive_map_app
package.domain = org.example
source.dir = src
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivy_garden.mapview
orientation = portrait
fullscreen = 1
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

[buildozer]
log_level = 2
warn_on_root = 1
requirements = python3,kivy,kivy_garden.mapview
android.archs = armeabi-v7a, arm64-v8a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 21b
android.private_storage = 1