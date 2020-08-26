bbcode-highlighter
==================
Visual Studio Code syntax highlighting support for FurAffinity's estoeric form of BBCode. This is a VS Code TextMate Language extension.

The Important Files
-------------------
The main file in this project is [`syntaxes/bbcode.tmLanguage.pyson`](syntaxes/bbcode.tmLanguage.pyson)[<sup>1</sup>](#pyson-files). That contains the syntax definitions for all the different elements. The equivalent JSON represntation is right alongside it (this is the file that actually is used by VS Code).

The Syntax
----------
This highlighter supports pretty much all the special syntax features that FurAffinity has to offer. I shall outline them below.

### Text Formatting
`[b]bold text[/b]` -> **bold text**<br>
`[i]italic text[/i]` -> *italic text*<br>
`[u]underline text[/u]` -> <u>underline text</u><br>
`[s]strikethru text[/s]` -> ~~strikethru text~~
`[sup]superscript text[/sup]` -> <sup>superscript text</sup><br>
`[sub]subscript text[/sub]` -> <sub>subscript text</sub><br>

### Colored Text
`[color=green]green text[/color]`<br>
See the full list of supported colors [here](https://www.furaffinity.net/view/10988173/).<br>
You can also use hex codes, such as `#a1f309` in place of the color name.

### Spoilers
`[spoiler]spoilers![/spoiler]`<br>
You can add a black box over text which disappears when you hover over it with your mouse.

### Character Shortcuts
`(C)` -> ©<br>
`(TM)` -> ™<br>
`(R)` -> ®<br>
These shortcuts are all case-insensitive.

### Headers
`[h1]Heading 1[/h1]`<br>
Headers `h1` through `h5` are all supported.

### Text Alignment
`[left]Left-aligned text (default)[/left]`
`[right]Right-aligned text[/right]`
`[center]Centered text[/center]`

### Quotes
##### Version 1
`[quote]Some quoted text[/quote]`<br>
↓
> Some quoted text

<br>

##### Version 2
`[quote=Raptor]Some quoted text[/quote]`<br>
↓
> ***Raptor wrote:***<br>
> Some quoted text

### Links
FurAffinity automatically recognizes raw links, such as [www.furaffinity.net](www.furaffinity.net), and also emails, such as [someone@example.com](mailto:someone@example.com) In addition, you can also use the `url` tag:<br>
`[url=https://www.furaffinity.net/user/raptor4694]Raptor's profile[/url]` -> [Raptor's profile](https://www.furaffinity.net/user/raptor4694)

Relative links are supported, so doing `[url=/user/raptor4694]Raptor's profile[/url]` would also work.

### YouTube Video Embedding
`[yt]https://www.youtube.com/watch?v=T8rSVrLzsK4[/yt]`<br>
This feature only works within journals.

### User Mentions
The number of icons you can get per post is limited.
##### Version 1
`:iconusername:` - replace 'username' with the user's lower name as it appears in their profile URL. Will result in their avatar followed by their username.<br>
`:usernameicon:` - like before, but only does the avatar.
`:linkusername:` - only does their name.

##### Version 2
`@username` - only does their name.<br>
`@@username` - does their avatar *and* username.

### Comic Navigation
`[previous, first, next]`<br>
Replace `previous`, `first`, and `next` with either a single dash ('-') or a submission ID. Use a dash if that part is invalid or unavailable. Submission IDs are the number in the URL of the submission (for example, in the submission [https://www.furaffinity.net/view/37557279/](https://www.furaffinity.net/view/37557279/), `37557279` would be the submission ID).<br>
This feature only works within gallery/scraps post descriptions.

### Horizontal Lines
Putting 5 or more dashes (`-----`) on a line by themselves creates a horizontal separator.

TextMate Scopes
---------------
This section is for users to reference when designing color themes in VS Code.

The global scope is `source.bb`.

### Blocks
For every tag, the following scopes apply:<br>
```
[example]blahblahblah[/example]
```
The brackets around the opening tag `[` and `]` are scoped as `punctuation.brackets.tag.begin.bb`.<br>
The brackets around the closing tag `[` and `]` are scoped as `punctuation.brackets.tag.end.bb`.<br>
The name of the opening tag `example` is scoped as `entity.name.tag.open.bb`.<br>
The name of the closing tag `/example` is scoped as `entity.name.tag.close.bb`.<br>

For tags with an attribute, the following additional scopes apply:<br>
```
[example=Some Attribute]blahblahblah[/example]
```
The equal sign `=` is scoped as `keyword.operator.attribute.bb`.<br>

### Tag Contents
The contents of the `[b]`, `[i]`, `[u]`, `[sup]`, `[sub]`, and `[s]` tags are scoped as their corresponding markdown syntax would be. For example, the text within `[i]blahblahblah[/i]` ("blahblahblah") would be scoped as `markup.italic.bb`.

Here's a table containing the scopes for the contents of each tag:
| Tag Name    | TM Scope              |
| ----------- | --------------------- |
| `[b]`       | markup.bold.bb        |
| `[i]`       | markup.italic.bb      |
| `[u]`       | markup.underline.bb   |
| `[s]`       | markup.strikethru.bb  |
| `[sup]`     | markup.superscript.bb |
| `[sub]`     | markup.subscript.bb   |
| `[spoiler]` | markup.spoiler.bb     |

### The [color] Tag
The name of the color within `[color=name]blahblahblah[/color]` tags has its own unique scope. The scope is in the format `support.color.NAME.bb` where NAME is the (lowercase) name of the valid color used. Only supported colors get scoped like this. Invalid colors get scoped as `invalid.illegal.color.bb`.

Hex colors such as `#f0a382` get scoped as `constant.other.color.bb`.

The contents of `[color]` tags get scoped as `markup.color.bb`.

### The [quote] Tag
The contents of the attribute in `[quote=]` tags are scoped as `string.unquoted.username.bb`.

### User Mentions
User mentions get scoped as `markup.usertag.bb`.

### Headers
The contents of the header tags get scoped as `markup.header#.bb` where `#` is the header number from 1 to 5.

### Links
Links (whether raw or as the attribute/tag contents of `[url]` or `[yt]` tags) get scoped as `markup.underline.link.bb`. Emails are scoped as `markup.underline.link.email.bb`.

### Horizontal Lines
Horizontal lines are scoped as `keyword.operator.horizontal-line.bb`.

### Invalid Tags
Invalid opening/unmatched closing tags get scoped as `invalid.illegal.tag.bb`. This includes tags such as `[color]` (missing the attribute) and `[/center]` (missing opening tag).

### Navigation Buttons
For navigation buttons, the following scopes apply:<br>
```
[37557279, -, 36718054]
```
The opening bracket '`[`' is scoped as `punctuation.brackets.navigation.begin.bb`.<br>
The closing bracket '`]`' is scoped as `punctuation.brackets.navigation.end.bb`.<br>
Submission ID numbers are scoped as `entity.name.submission-id.bb`.<br>
The commas '`,`' are scoped as `punctuation.separator.navigator-submission.bb`.<br>
The dashes '`-`' are scoped as `keyword.operator.disabled-submission-id.bb`.

#### PySON Files
<small>PySON is in a special data format I developed myself called PySON (Python Serialized Object Notation). It's easier to write than JSON but converts right back to it. I'll link to the PySON project here when I post it - I have a converter tool (written in Python) and also a VS Code syntax highlighting extension as well.</small>
