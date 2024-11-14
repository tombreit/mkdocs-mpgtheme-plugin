# SPDX-FileCopyrightText: 2024 Thomas Breitner
#
# SPDX-License-Identifier: MIT

"""
MkDocs MPG Theme Plugin
"""

import shutil
from pathlib import Path
from mkdocs.plugins import BasePlugin


class MpgThemePlugin(BasePlugin):
    def on_files(self, files, config):
        plugin_dir = Path(__file__).parent

        # TODO: Test if assets could be placed under custom_dir
        # Copy theme files to site directory
        theme_dir = plugin_dir / "assets" / "mpgtheme"
        target_dir = Path(config["site_dir"]) / "assets" / "mpgtheme"
        shutil.copytree(theme_dir, target_dir, dirs_exist_ok=True)

        return files

    def on_config(self, config):
        """Modify the MkDocs config when the plugin loads"""
        # Get plugin directory
        plugin_dir = Path(__file__).parent

        # Set custom override theme directory
        custom_dir = plugin_dir / "mpgtheme"
        config.theme.dirs.insert(0, str(custom_dir.resolve()))

        # Add custom CSS
        config["extra_css"] = ["assets/mpgtheme/css/mpg.css"] + config["extra_css"]

        return config
