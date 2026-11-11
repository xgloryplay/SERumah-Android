#!/usr/bin/env python3

import sys
from pathlib import Path
import xml.etree.ElementTree as ET

manifest_path = Path(sys.argv[1])

ET.register_namespace(
    "android",
    "http://schemas.android.com/apk/res/android"
)

tree = ET.parse(manifest_path)
root = tree.getroot()

android = "{http://schemas.android.com/apk/res/android}"

# Pastikan fitur NFC bersifat opsional.
feature_name = "android.hardware.nfc"

features = root.findall("uses-feature")
found = False

for feature in features:
    if feature.get(android + "name") == feature_name:
        feature.set(android + "required", "false")
        found = True

if not found:
    feature = ET.Element("uses-feature")
    feature.set(android + "name", feature_name)
    feature.set(android + "required", "false")

    root.insert(0, feature)

tree.write(
    manifest_path,
    encoding="utf-8",
    xml_declaration=True
)

print("Android manifest updated successfully.")