# afinadorOGG
## Synopsis
Python application that tunes cello strings to natural frequencies accessible via ogg files.

## Code Example

```python
	def play_sound(self, frequency):
        pipeline = Gst.Pipeline(name='note')
        pipeline = Gst.ElementFactory.make("playbin", "player")
        pipeline.set_property('uri', 'file://' + os.path.abspath(frequency + '.ogg'))
        pipeline.set_state(Gst.State.PLAYING)
```  
  
## Motivation

Tune a cello with natural string frequencies.

## Installation
N/A

## Contributors

elbillyto
## License

This document and the project files are not copyrighted and are released into the public domain.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
