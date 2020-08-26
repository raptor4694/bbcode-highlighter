from typing import Set, Dict, Union, Literal
from pprint import pprint
from pyperclip import copy
import re

def make_regex(options: Set[str]) -> str:
    Group = Dict[str, Union['Group', Literal[1]]]

    def make_groups(options: Set[str]) -> Group:
        groups: Group = {}
        for option in options:
            group = groups
            for ch in option:
                group2 = group.get(ch)
                if group2 is None:
                    group[ch] = group2 = {}
                group = group2
            group[''] = 1
        return groups

    def condense_groups(groups: Group) -> Group:
        newgroups: Group = {}
        for key, value in groups.items():
            print(f"visit {key!r} = ", end='')
            pprint(value)
            if not isinstance(value, dict):
                result = newgroups[key] = value
            elif len(value) == 1:
                while len(value) == 1:
                    key2, value2 = next(iter(value.items()))
                    if key2 == '':
                        value = newgroups[key] = value2
                        break
                    elif not isinstance(value2, dict):
                        value = value2
                        key += key2
                        break
                    else:
                        value = condense_groups(value2)
                        key += key2
                result = newgroups[key] = value
            else:
                result = newgroups[key] = condense_groups(value)
            print(f"result of {key!r} = ", end='')
            pprint(result)
        return newgroups

    def compile_groups(groups: Group) -> str:
        if len(groups) == 1:
            key, value = next(iter(groups.items()))
            if not isinstance(value, dict):
                return key
            else:
                return key + compile_groups(value)
        else:
            result = "(?:"
            first = True
            for key, value in sorted(groups.items(), key=lambda x: x[0]):
                if first: first = False
                else: result += "|"
                if not isinstance(value, dict):
                    result += key
                else:
                    result += key + compile_groups(value)
            result += ")"
            return result

    groups = make_groups(options)
    groups = condense_groups(groups)

    return compile_groups(groups)

colors = {
    'aliceblue',
    'antiquewhite',
    'aqua',
    'aquamarine',
    'azure',
    'beige',
    'bisque',
    'black',
    'blanchedalmond',
    'blue',
    'blueviolet',
    'brown',
    'burlywood',
    'cadetblue',
    'chartreuse',
    'chocolate',
    'coral',
    'cornflowerblue',
    'cornsilk',
    'crimson',
    'cyan',
    'darkblue',
    'darkcyan',
    'darkgoldenrod',
    'darkgray',
    'darkgreen',
    'darkkhaki',
    'darkmagenta',
    'darkolivegreen',
    'darkorange',
    'darkorchid',
    'darkred',
    'darksalmon',
    'darkseagreen',
    'darkslateblue',
    'darkslategray',
    'darkturquoise',
    'darkviolet',
    'deeppink',
    'deepskyblue',
    'dimgray',
    'dodgerblue',
    'firebrick',
    'floralwhite',
    'forestgreen',
    'fuchsia',
    'gainsboro',
    'ghostwhite',
    'gold',
    'goldenrod',
    'gray',
    'green',
    'greenyellow',
    'honeydew',
    'hotpink',
    'indianred',
    'indigo',
    'ivory',
    'khaki',
    'lavender',
    'lavenderblush',
    'lawngreen',
    'lemonchiffon',
    'lightblue',
    'lightcoral',
    'lightcyan',
    'lightgoldenrodyellow',
    'lightgray',
    'lightgreen',
    'lightpink',
    'lightsalmon',
    'lightseagreen',
    'lightskyblue',
    'lightslategray',
    'lightsteelblue',
    'lightyellow',
    'lime',
    'limegreen',
    'linen',
    'magenta',
    'maroon',
    'mediumaquamarine',
    'mediumblue',
    'mediumorchid',
    'mediumpurple',
    'mediumseagreen',
    'mediumslateblue',
    'mediumspringgreen',
    'mediumturquoise',
    'mediumvioletred',
    'midnightblue',
    'mintcream',
    'mistyrose',
    'moccasin',
    'navajowhite',
    'navy',
    'oldlace',
    'olive',
    'olivedrab',
    'orange',
    'orangered',
    'orchid',
    'palegoldenrod',
    'palegreen',
    'paleturquoise',
    'palevioletred',
    'papayawhip',
    'peachpuff',
    'peru',
    'pink',
    'plum',
    'powderblue',
    'purple',
    'red',
    'rosybrown',
    'royalblue',
    'saddlebrown',
    'salmon',
    'sandybrown',
    'seagreen',
    'seashell',
    'sienna',
    'silver',
    'skyblue',
    'slateblue',
    'slategray',
    'snow',
    'springgreen',
    'steelblue',
    'tan',
    'teal',
    'thistle',
    'tomato',
    'turquoise',
    'violet',
    'wheat',
    'white',
    'whitesmoke',
    'yellow',
    'yellowgreen',
}

re.compile(r'''(?x)
      (\[) (color) (=)
      (?:
        (\#[a-fA-F0-9]{6})
        | ((?:a(?:liceblue|ntiquewhite|qua(?:|marine)|zure)|b(?:eige|isque|l(?:a(?:ck|nchedalmond)|ue(?:|violet))|rown|urlywood)|c(?:adetblue|h(?:artreuse|ocolate)|or(?:al|n(?:flowerblue|silk))|rimson|yan)|d(?:ark(?:blue|cyan|g(?:oldenrod|r(?:ay|een))|khaki|magenta|o(?:livegreen|r(?:ange|chid))|red|s(?:almon|eagreen|late(?:blue|gray))|turquoise|violet)|eep(?:pink|skyblue)|imgray|odgerblue)|f(?:irebrick|loralwhite|orestgreen|uchsia)|g(?:ainsboro|hostwhite|old(?:|enrod)|r(?:ay|een(?:|yellow)))|ho(?:neydew|tpink)|i(?:ndi(?:anred|go)|vory)|khaki|l(?:a(?:vender(?:|blush)|wngreen)|emonchiffon|i(?:ght(?:blue|c(?:oral|yan)|g(?:oldenrodyellow|r(?:ay|een))|pink|s(?:almon|eagreen|kyblue|lategray|teelblue)|yellow)|me(?:|green)|nen))|m(?:a(?:genta|roon)|edium(?:aquamarine|blue|orchid|purple|s(?:eagreen|lateblue|pringgreen)|turquoise|violetred)|i(?:dnightblue|ntcream|styrose)|occasin)|nav(?:ajowhite|y)|o(?:l(?:dlace|ive(?:|drab))|r(?:ange(?:|red)|chid))|p(?:a(?:le(?:g(?:oldenrod|reen)|turquoise|violetred)|payawhip)|e(?:achpuff|ru)|ink|lum|owderblue|urple)|r(?:ed|o(?:sybrown|yalblue))|s(?:a(?:ddlebrown|lmon|ndybrown)|ea(?:green|shell)|i(?:enna|lver)|kyblue|late(?:blue|gray)|now|pringgreen|teelblue)|t(?:an|eal|histle|omato|urquoise)|violet|wh(?:eat|ite(?:|smoke))|yellow(?:|green)))
        | ([^\]]*)
      )
      (\])
    ''')

# regex = make_regex(colors)
# print(regex)
# copy(regex)