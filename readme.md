# Rescue old chests for 1.8

Quick and dirty thing that preserves chest contents for opening worlds from <u>1.7 or older</u> in <u>1.8 thru 1.14</u>. **If you are okay with skipping to <u>1.15 or later</u>, you don't need to run this script.**

Chests created in very early versions of minecraft didn't have data on which way they faced, so, left unchanged, they retained the block id 54:0 going into the anvil format. This caused them to be deleted upon opening a world in release 1.8 or later, and was only solved in 1.15. [MC-123686](https://bugs.mojang.com/browse/MC/issues/MC-123686); [MC-70813](https://bugs.mojang.com/browse/MC/issues/MC-70813) [MC-73053](https://bugs.mojang.com/browse/MC/issues/MC-73053) [MC-72484](https://bugs.mojang.com/browse/MC/issues/MC-72484)

This script changes them all to face east, which will at least let you keep your items. Double chests that should face north or south will render wrong but still work. Just take the stuff out and replace them whenever you see it. 

I don't understand why MCEdit won't just let me find/replace 54:0 with 54:5 but this script works so here it is.

This code was very loosely adapted from the functional part at the end of this C# script: https://gist.github.com/Gargaj/2891b8fc558e01b8ddf2 which can no longer be compiled because its relevant libraries seem to be gone or something. Or maybe I just don't want to go to the trouble of setting up a way to compile C# scripts just to do something that should be possible through MCEdit. Oh sure it's less performant, it's python running on python, but whatever, this is like a one-time thing people will only have to do once in their lives.

# How to use

1. Install the latest build of MCEdit 1.X: https://github.com/Podshot/MCEdit-Unified/releases -- I HAVE NO IDEA IF THIS WORKS ON MCEDIT 2.X, which is the download that appears if you google "download MCEdit".
2. Download `RescueChests18.py` from this repository. Here's how to download files from GitHub: https://docs.github.com/en/repositories/working-with-files/using-files/downloading-files-from-github
3. Put `RescueChests18.py` in your MCEdit installation's `/stock-filters/` folder. Be careful when dragging! The `.pyc` files in that folder may try to execute when stuff gets dragged on them.
4. **BACK UP YOUR WORLD.** YOU CAN DO THIS BY DUPLICATING THE WORLD FOLDER AND GIVING IT A NEW NAME.
5. Open the backup of your world in MCEdit.
6. Uncheck `Undo ✅` on the top bar; this is optional but MCEdit runs slower when it tries to cache your history, and it's not necessary because you BACKED UP YOUR WORLD.
7. Select all by pressing `CTRL`+`A`.
8. Click the coffeepot to switch to filter mode.
9. Select `Rescue old chests for 1.8` from the dropdown and execute it.
10. Wait a really long time. Don't worry, it didn't crash, it's just doing its thing.
11. Press save! That's `CTRL`+`S`, but the bottom left corner of MCEdit will tell you that.
12. Wait a really long time but this time it has a progress bar.
13. Now you should be able to open the world in 1.8-1.14 with your chests recovered, even if they're facing a weird direction.

LICENSE:
do whatever you want with it. THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

