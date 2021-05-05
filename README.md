# Amiga 4000 Bill of Material

This project contains the Bill of Material for building an own **Amiga 4000 Desktop Rev. B** mainboard.

**IMPORTANT:** This project is still **work in progress** at the moment. Please do not rely solely on this list, but compare it with other bill of materials.

* [Read as self-contained HTML](bom/a4000-bom.html)
* [Read inline as Markdown](bom/a4000-bom.md)

## Read Me First!

If you want to build your own Amiga, be aware that the machine was designed in the early 1990s. While almost all of the standard components are still available today, other components are very rare by now.

You will need all of the listed components for a working mainboard. We recommend that you try to get the components marked as "rare" first, so you won't waste your money on standard components if you fail to get all the rare ones.

Also be aware that there are six PALs on the list. While the JEDEC files are [available at the Amiga Wiki](http://www.amigawiki.de/doku.php?id=en:parts:pld_download#a4000), a GAL capable programmer is required for "flashing" the corresponding GALs. They cannot be programmed in-circuit. We also recommend to use PLCC sockets, as it might turn out after first tests that they need to be reprogrammed.

This bill of material only comprises of the components required for the mainboard itself. **The absolute bare minimum for a working machine is:**

* This mainboard, fully assembled and tested
* A power supply
* A CPU board
* One 2MB SIMM for the Chip RAM

For a complete Amiga 4000D you also need:

* A computer case (and the skills to make it fit unless it's the original case)
* One to four 4MB SIMMs for Fast RAM
* An Amiga 4000 daughterboard
* An Amiga keyboard and Amiga mouse
* Hard disk drives and floppy disk drives at your discretion

See [this article](http://amigadev.elowar.com/read/ADCD_2.1/AmigaMail_Vol2_guide/node0162.html) for the SIMM types.

## Battery and Capacitors

This Bill of Material includes a NiCd battery as buffer for the RTC. These batteries tend to leak over the years, and certainly killed a lot of classic Amiga 4000s. It is advisable to use a different type of energy source, like a button cell. However, the necessary components and modifications are *not* a part of this project.

This list also includes regular electrolytic capacitors, which may leak and cause damage over the years as well. Some people prefer to use ceramic capacitors instead. They cannot leak, but *may* cause other problems. There are good arguments for both types, so the final choice is up to you. However, if you decide to use electrolytic capacitors, we recommend to get the best quality that money can buy.

## Contribute

This list is meant to be a community work. Our goal is to have a canonical list that people can rely on when ordering parts for building an own Amiga 4000D mainboard.

However, this list may not be free of errors. If you have found one, please [open an issue](https://github.com/shred/a4000-bom/issues) or send a patch.

## Disclaimer

This is not an official list! It was collected and reviewed by Amiga enthusiasts.

Although we strive to make the information in this project as helpful and accurate as possible, it is provided "as is" and without warranties of any kind either expressed or implied.

In other words: You might spend a lot of money and end up with a cardboard box full of useless components.

**Use at your own risk!**

## Sources

The following sources have been used:

* AmigaWiki's [A4000 Rev B Schematic](http://www.amigawiki.de/dnl/schematics/A4000_Rb.pdf)
* Acill's [A4000 Replica Project](https://github.com/Acill/A4000RevB)

## Technical Background

The main file of this project is the `a4000-rb-bom.yml` file. It contains the bill of material in a file format that can be easily diffed by git, and can also easily read by programs.

A Python tool called `convert.py` generates human readable files from that. You can find them in the `bom` directory. The converter needs [PyYAML](https://pypi.org/project/PyYAML/) and [Jinja2](https://pypi.org/project/Jinja2/) installed.

## Copyright

This project is released under the terms of the [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
