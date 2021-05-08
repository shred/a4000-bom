# Table of Contents

<div class="toc"><ul>
  <li><a href="index.html">Introduction</a> &ndash; this page</li>
  <li><a href="a4000-bom.html">The Bill of Material</a> &ndash; what you are probably here for</li>
  <li><a href="csv.html">CSV Export</a> &ndash; for Mouser Electronics</li>
  <li><a href="https://github.com/shred/a4000-bom">GitHub Project Page</a> &ndash; feel free to contribute</li>
</ul></div>

# Introduction

This is the Bill of Material for a replica Amiga 4000D Rev B. It bases on the [Amiga 4000 Schematics](http://www.amigawiki.de/dnl/schematics/A4000_Rb.pdf) found at the Amiga Wiki, and is optimized for [Acill's A4000 Replica Project](https://github.com/Acill/A4000RevB) boards.

## Read Me First!

If you want to build your own Amiga, be aware that the machine was designed in the early 1990s. While almost all of the standard components are still available today, some components are very rare by now.

You will need all of the listed components for a working mainboard. We recommend that you try to get the components marked as <span class="rare">Rare</span> first, so you won't waste your money on standard components if you fail to get all the rare ones.

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

This Bill of Material includes a NiCd battery as buffer for the RTC. These batteries tend to leak over the years, and certainly killed a lot of classic Amiga 4000s. It is advisable to use a different type of energy source, like a button cell. However, the necessary components and modifications are *not* part of this project.

This list also includes regular electrolytic capacitors, which may leak and cause damage over the years as well. Some people prefer to use ceramic capacitors instead. They cannot leak, but *may* cause other problems. There are good arguments for both types, so the final choice is up to you. However, if you decide to use electrolytic capacitors, we recommend to get the best quality that money can buy.

## Disclaimer

This is not an official list! It was collected and reviewed by Amiga enthusiasts.

Although we strive to make the information in this project as helpful and accurate as possible, it is provided "as is" and without warranties of any kind either expressed or implied.

In other words: You might spend a lot of money, and end up with a non-functioning mainboard or a cardboard box full of useless components.

**Use at your own risk!**

## Contribute

This list is meant to be a community work. Our goal is to have a canonical list that people can rely on when ordering parts for building an own Amiga 4000D mainboard.

However, this list may not be free of errors. If you have found one, please [open an issue](https://github.com/shred/a4000-bom/issues), send a patch, or [send me a message](https://www.a1k.org/forum/index.php?members/6632/) at the A1K.org forum.

## License

This project is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).
