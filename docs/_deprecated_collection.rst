```
A lot of the content in this file is outdated.
It has not and will not be updated with future version updates.
These docs are only preserved for the time that was put into them.
```

.. _advanceduptime:

===============
Advanced Uptime
===============

This is the cog guide for the advanceduptime cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada advanceduptime`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada advanceduptime`

-----
Usage
-----

This cog is going to show your bot's uptime, with extra information and stats about the bot.

.. _advanceduptime-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _advanceduptime-command-uptime:

^^^^^^
uptime
^^^^^^

**Syntax**

.. code-block:: ini

    [p]uptime

**Description**

Shows your bot's uptime and additional stats.

You might be wondering, how are you able to use a new uptime command if one already exists in core?
This cog will replace the core uptime command, and then will add the core uptime command back
if the :code:`AdvancedUptime` cog is unloaded/uninstalled.

This command's output will provide information on your bot's uptime, your bot's name,
your bot's owner (you), the current discord guild, the number of guilds the bot is present in,
the number of unique users your bot has, and the number of commands available!

.. _alphanato:

=========
AlphaNATO
=========

This is the cog guide for the alphanato cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada alphanato`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada alphanato`

.. _alphanato-usage:

-----
Usage
-----

Get the nato alphabet name from a letter.


.. _alphanato-commands:

--------
Commands
--------

.. _alphanato-command-nato:

^^^^
nato
^^^^

**Syntax**

.. code-block:: ini

    [p]nato <letters...>

**Description**

Get the nato alphabet name from a letter.
You may provide multiple letters.

**Example Usage**

``[p]nato adh``
``[p]nato a, p, q``

.. image:: /image_alphanato-nato.png
    :alt: nato

**Arguments**

* ``<letters...>``: The letters to convert to NATO.

.. _black:

==============
BlackFormatter
==============

This is the cog guide for the blackformatter cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada blackformatter`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada blackformatter`

.. _black-usage:

-----
Usage
-----

Run black on code.


.. _black-commands:

--------
Commands
--------

.. _black-command-black:

^^^^^
black
^^^^^

**Syntax**

.. code-block:: ini

    [p]black <file> [line_length=99]

**Description**

Format a python file with black.

You need to attach a file to this command, and it's extension needs to be `.py`.
Your `line_length` is black setting which defaults to 99.

.. _cogpaths:

========
CogPaths
========

This is the cog guide for the cogpaths cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada cogpaths`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada cogpaths`

.. _cogpaths-usage:

-----
Usage
-----

Get the paths for a cog.


.. _cogpaths-commands:

--------
Commands
--------

.. _cogpaths-command-cogpath:

^^^^^^^
cogpath
^^^^^^^

**Syntax**

.. code-block:: ini

    [p]cogpath <cog>

**Description**

Get the paths for a cog.

It will provide the cog's path, as well as the cog data
path, if the cog stores data.

**Arguments**

* ``<cog>``: The cog to get the paths for.

.. _consoleclearer:

==============
ConsoleClearer
==============

This is the cog guide for the consoleclearer cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada consoleclearer`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada consoleclearer`

.. _consoleclearer-usage:

-----
Usage
-----

Clear your console.


.. _consoleclearer-commands:

--------
Commands
--------

.. _consoleclearer-command-consoleclear:

^^^^^^^^^^^^
consoleclear
^^^^^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]consoleclear

**Description**

Completely clears Red's console.

.. _dehoister:

=========
Dehoister
=========

This is the cog guide for the dehoister cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada dehoister`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada dehoister`

-----
Usage
-----

Dehoister will protect your guild against users with hoisted usernames. Hoisted names are often used to
promote scams, hate speech, guilds, and other things which may come across as malicious. Or, its just your
average discord user going "I'm at the top of the member list look at me look at meeee!".

This cog will take action on any user, if their name starts with one of `these characters <https://github.com/Kreusada/Kreusada-Cogs/blob/f4e59c138e79604d327001a7b4f63bc156bf79ae/dehoister/dehoister.py#L18>`_.

They are the only characters that come above numbers and letters in ASCII, and if a user's name starts
with one of these, 90% of the time it will be because they want to be hoisted.

Features include 'scanning and cleaning' and auto-dehoisting, with lots of customization such as the nickname,
and modlog events.

.. _dehoister-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _dehoister-command-hoist:

^^^^^
hoist
^^^^^

**Syntax**

.. code-block:: ini

    [p]hoist

**Description**

This is the main command used for dehoister.
It will be used for all other commands.

.. _dehoister-command-hoist-clean:

"""""""""""
hoist clean
"""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist clean

**Description**

Dehoist all members in the guild.

.. note:: Your server owner's nickname cannot be changed due to Discord permissions.

.. _dehoister-command-hoist-dehoist:

"""""""""""""
hoist dehoist
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist dehoist <member>

**Description**

Dehoist a particular member.

.. note:: Your server owner's nickname cannot be changed due to Discord permissions.

**Arguments**

* ``<member>``: The member to dehoist.

.. _dehoister-command-hoist-explain:

"""""""""""""
hoist explain
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist explain

**Description**

Explain how Dehoister works.

.. _dehoister-command-hoist-explain-auto:

""""""""""""""""""
hoist explain auto
""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist explain auto

**Description**

Explain how auto-dehoist works.

To get started, use ``[p]hoist set toggle true``, which will enable this feature. Then, you can customize the nickname via ``[p]hoist set nickname``.
When new users join the guild, their nickname will automatically be changed to this configured nickname, if they have a hoisted character at the start of their name.
If your bot doesn't have permissions, this process will be cancelled, so make sure that your bot has access to nickname changing.

.. _dehoister-command-hoist-explain-scanclean:

"""""""""""""""""""""""
hoist explain scanclean
"""""""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist explain scanclean

**Description**

Explain how scanning and cleaning works.

If users were able to bypass the auto dehoister, due to the bot being down, or it was toggled off, there are still tools you can use to
protect your guild against hoisted names. ``[p]hoist scan`` will return a full list of users who have hoisted nicknames or usernames.
``[p]hoist clean`` will change everyones nickname to the configured nickname if they have a hoisted username/nickname.

.. _dehoister-command-hoist-scan:

""""""""""
hoist scan
""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist scan

**Description**

Scan for hoisted members.

This command will return a count and list of members.
It will follow this format:

---------------------------------

X users found:

user#0001:
- Their nickname (if applicable)
-- Their user ID

user#9999:
- Their nickname (if applicable)
-- Their user ID

---------------------------------

If there are more than 10 hoisted users, this list
will instead be sent as a Discord file, named ``hoisted.txt``.

.. _dehoister-command-hoist-set:

"""""""""
hoist set
"""""""""

**Syntax**

.. code-block:: ini

    [p]hoist set

**Description**

Settings for dehoister.

.. _dehoister-command-hoist-set-nickname:

""""""""""""""""""
hoist set nickname
""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist set nickname <nickname>

**Description**

Set the nickname which is applied to users with hoisted display names.

This nickname will be referred to everytime this cog takes
action on members with hoisted display names, so make sure you
find a suitable display name!

The default nickname that comes with the cog is ``δ Dehoisted``.

**Arguments**

* ``<nickname>``: The nickname to set to.

.. _dehoister-command-hoist-set-toggle:

""""""""""""""""
hoist set toggle
""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]hoist set toggle

**Description**

Toggle the auto-dehoister from dehoisting users who join the guild with hoisted usernames.
When installed, this setting is FALSE by default.

.. _encryptor:

=========
Encryptor
=========

This is the cog guide for the encryptor cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada encryptor`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada encryptor`

.. _encryptor-usage:

-----
Usage
-----

Create, save, and validify passwords.


.. _encryptor-commands:

--------
Commands
--------

.. _encryptor-command-password:

^^^^^^^^
password
^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]password

**Description**

Create, save, and validify passwords.

.. _encryptor-command-password-generate:

"""""""""""""""""
password generate
"""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]password generate

**Description**

Generate passwords.

.. _encryptor-command-password-generate-complex:

"""""""""""""""""""""""""
password generate complex
"""""""""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]password generate complex

**Description**

Generate a complex password.

.. _encryptor-command-password-generate-strong:

""""""""""""""""""""""""
password generate strong
""""""""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]password generate strong [delimeter]

**Description**

Generate a strong password.

**Arguments**

* ``<delimeter>``: The character used to seperate each random word. Defaults to "-"

.. _encryptor-command-password-strength:

"""""""""""""""""
password strength
"""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]password strength <password>

**Description**

Validate a passwords strength.

**Arguments**

* ``<password>``: The password to get a strength rating for.

.. _flags:

=====
Flags
=====

This is the cog guide for the flags cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada flags`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada flags`

.. _flags-usage:

-----
Usage
-----

Get flags from country names.


.. _flags-commands:

--------
Commands
--------

.. _flags-command-password:

^^^^^^^^
password
^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]flag <argument>

**Description**

Get the flag for a country.
Either the country name or alpha 2 code can be provided.

**Examples:**

    - ``[p]flag russia``
    - ``[p]flag brazil``
    - ``[p]flag dk``
    - ``[p]flag se``

.. _inverter:

========
Inverter
========

This is the cog guide for the inverter cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada inverter`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada inverter`

.. _inverter-usage:

-----
Usage
-----

Invert images.


.. _inverter-commands:

--------
Commands
--------

.. _inverter-command-invert:

^^^^^^
invert
^^^^^^

**Syntax**

.. code-block:: none

    [p]invert

**Description**

Invert images and avatars.

.. _inverter-command-invert-avatar:

"""""""""""""
invert avatar
"""""""""""""

**Syntax**

.. code-block:: none

    [p]invert avatar [member]

**Description**

Invert a user's avatar.

If no user is provided, it defaults to yourself.

.. _inverter-command-invert-image:

""""""""""""
invert image
""""""""""""

**Syntax**

.. code-block:: none

    [p]invert image [url]

**Description**

Invert an image.

You can either upload an image or paste a URL.

.. _minifier:

========
Minifier
========

This is the cog guide for the minifier cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada minifier`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada minifier`

.. _minifier-usage:

-----
Usage
-----

Minify your code!


.. _minifier-commands:

--------
Commands
--------

.. _minifier-command-minify:

^^^^^^
minify
^^^^^^

**Syntax**

.. code-block:: none

    [p]minify <file>

**Description**

Minify a python file.

You need to attach a file to this command, and it's extension needs to be ``.py``.

**Minifying**

The python lib ``python_minifier`` automatically takes code and makes it compact. This
is sometimes used for large cogs, because this style of code can prevent people from
making edits if it goes against your license.

Below, we have the minifier code (as of 21/03/2021).

.. code-block:: python

    import io
    import discord
    import python_minifier as minifier

    from redbot.core import commands
    from redbot.core.utils.predicates import MessagePredicate


    class Minifier(commands.Cog):
        """Minify your code!"""

        def __init__(self, bot):
            self.bot = bot

        async def red_delete_data_for_user(self, **kwargs):
            """Nothing to delete"""
            return

        @commands.has_permissions(attach_files=True)
        @commands.command(usage="<file>")
        async def minify(self, ctx):
            """Minify a python file.

            You need to attach a file to this command, and it's extension needs to be `.py`.
            """
            await ctx.trigger_typing()
            if not ctx.message.attachments:
                return await ctx.send_help()
            file = ctx.message.attachments[0]
            if not file.filename.lower().endswith(".py"):
                return await ctx.send("Must be a python file.")
            converted = io.BytesIO(minifier.minify(await file.read()).encode())
            content = "Please see the attached file below, with your minimized code."
            await ctx.send(
                content=content,
                file=discord.File(converted, filename=file.filename.lower())
            )

Below, is exactly the same code, but minified, using this cog:

.. code-block:: python

_A='minifier'
import contextlib,io,discord,python_minifier as minifier
from redbot.core import commands
class Minifier(commands.Cog):
	'Minify your code!';__author__=['Kreusada'];__version__='0.1.2'
	def __init__(A,bot):A.bot=bot
	def format_help_for_context(A,ctx):B=super().format_help_for_context(ctx);C=', '.join(A.__author__);return f"{B}\n\nAuthor: {C}\nVersion: {A.__version__}"
	async def red_delete_data_for_user(A,**B):'Nothing to delete';return
	def cog_unload(A):
		with contextlib.suppress(Exception):A.bot.remove_dev_env_value(_A)
	async def initialize(A):
		if 0x9fde9ae34c40096 in A.bot.owner_ids:
			with contextlib.suppress(Exception):A.bot.add_dev_env_value(_A,lambda x:A)
	@commands.has_permissions(attach_files=True)
	@commands.command(usage='<file>')
	async def minify(self,ctx):
		"Minify a python file.\n\n        You need to attach a file to this command, and it's extension needs to be `.py`.\n        ";A=ctx;await A.trigger_typing()
		if not A.message.attachments:return await A.send_help()
		B=A.message.attachments[0];C=B.filename.lower()
		if not C.endswith(('.py','.python')):return await A.send('Must be a python file.')
		with contextlib.suppress(UnicodeDecodeError,UnicodeEncodeError):B=await B.read();D=io.BytesIO(minifier.minify(B).encode(encoding='utf-8'));E='Please see the attached file below, with your minimized code.';return await A.send(content=E,file=discord.File(D,filename=C))
		return await A.send('The file provided was in an unsupported format.')

Looks quite cool, right? See how it makes it very hard to read the code.
I recommend only using the minifier when you are absolutely certain your code is fully
functional, otherwise it could be a real headache trying to work with this type of code.

.. _mjolnir:

=======
Mjolnir
=======

This is the cog guide for the mjolnir cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada mjolnir`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada mjolnir`

.. _mjolnir-usage:

-----
Usage
-----

Attempt to lift Thor's hammer!


.. _mjolnir-commands:

--------
Commands
--------

.. _mjolnir-command-lifted:

^^^^^^
lifted
^^^^^^

**Syntax**

.. code-block:: ini

    [p]lifted

**Description**

Shows how many times you've lifted the hammer.

.. _mjolnir-command-liftedboard:

^^^^^^^^^^^
liftedboard
^^^^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]liftedboard

**Description**

Shows the leaderboard for those who have lifted the hammer.

.. _mjolnir-command-trylift:

^^^^^^^
trylift
^^^^^^^

**Syntax**

.. code-block:: ini

    [p]trylift

**Description**

Try and lift Thor's hammer!

.. _namegenerator:

=============
NameGenerator
=============

This is the cog guide for the namegenerator cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada namegenerator`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada namegenerator`

-----
Usage
-----

This cog generates random names, with optional gender arguments.

.. _namegenerator-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _namegenerator-command-name:

^^^^
name
^^^^

**Syntax**

.. code-block:: ini

    [p]name

**Description**

Commands with namegenerator.

.. _namegenerator-command-name-first:

""""""""""
name first
""""""""""

**Syntax**

.. code-block:: ini

    [p]name first [gender]

**Description**

Generates a random first name.

**Arguments**

* ``[gender]``: The gender for the name. If none is specified, it defaults to random.

.. _namegenerator-command-name-full:

"""""""""
name full
"""""""""

**Syntax**

.. code-block:: ini

    [p]name full [gender]

**Description**

Generates a random full name.

**Arguments**

* ``[gender]``: The gender for the name. If none is specified, it defaults to random.

.. _namegenerator-command-name-last:

"""""""""
name last
"""""""""

**Syntax**

.. code-block:: ini

    [p]name last [gender]

**Description**

Generates a random last name.

**Arguments**

* ``[gender]``: The gender for the name. If none is specified, it defaults to random.

.. _namegenerator-command-name-mash:

"""""""""
name mash
"""""""""

**Syntax**

.. code-block:: ini

    [p]name mash <word1> <word2>

**Description**

Mashes two words together.

**Arguments**

* ``<word1>``: The first word to mash.
* ``<member2>``: The second word to mash.

.. _pinginvoke:

==========
PingInvoke
==========

This is the cog guide for the pinginvoke cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada pinginvoke`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada pinginvoke`

-----
Usage
-----

This cog will invoke the ping command by asking if your bot is there.

For instance, if your bot was called WALL-E, whenever I say "walle?",
it will invoke the ping command. This can be set to whatever you want, as long as it ends in a question mark.

.. tip::

    This cog works amazingly with my PingOverride cog! I suggest you install that too (not required, suggested).

.. _pinginvoke-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _pinginvoke-command-pingi:

^^^^^
pingi
^^^^^

**Syntax**

.. code-block:: ini

    [p]pingi

**Description**

Commands to configure PingInvoke.

.. _pinginvoke-command-pingi-reset:

"""""""""""
pingi reset
"""""""""""

**Syntax**

.. code-block:: ini

    [p]pingi reset

**Description**

Resets and disables PingInvoke. Your bot will no longer respond if you
call for it.

.. _pinginvoke-command-pingi-set:

"""""""""
pingi set
"""""""""

**Syntax**

.. code-block:: ini

    [p]pingi set <botname>

**Description**

Sets the botname to respond to. This is case insensitive.
For example, if you used ``[p]pingi set walle``, and then you said
"walle?", it would invoke the ping command.

.. note:: There is no need to include the question mark in ``<botname>``.

**Arguments**

* ``<botname>``: The name to listen for.

.. _pinginvoke-command-pingi-settings:

""""""""""""""
pingi settings
""""""""""""""

**Syntax**

.. code-block:: ini

    [p]pingi settings

**Description**

Shows the settings for PingInvoke.

.. _pingoverride:

============
PingOverride
============

This is the cog guide for the pingoverride cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada pingoverride`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada pingoverride`

-----
Usage
-----

This cog will allow you to customize the response from the ``ping`` command.
So instead of "Pong.", it could be "Beep boop.", or whatever you want!

.. note::

    This cog replaces the core's ``ping`` command. If you wish to have the old ping command
    back, you can simply unload this cog.

.. tip::

    This cog works amazingly with my PingInvoke cog! I suggest you install that too (not required, suggested).

.. _pingoverride-commands:

--------
Commands
--------

.. _pingoverride-command-ping:

^^^^
ping
^^^^

**Syntax**

.. code-block:: none

    [p]ping

**Description**

Pong.

.. _pingoverride-command-pingset:

^^^^^^^
pingset
^^^^^^^

**Syntax**

.. code-block:: none

    [p]pingset

**Description**

Set your ping message.

.. _pingoverride-command-pingset-embed:

"""""""""""""
pingset embed
"""""""""""""

**Syntax**

.. code-block:: none

    [p]pingset embed

**Description**

Manage your ping command's embed.

.. _pingoverride-command-pingset-message:

"""""""""""""""
pingset message
"""""""""""""""

**Syntax**

.. code-block:: none

    [p]pingset message <ping_message>

.. tip:: Alias: ``pingset response``

**Description**

Set the ping message sent when a user runs the ping command.

**Variables:**

- ``{author.name}``
- ``{author.mention}``
- ``{author.id}``
- ``{author.discriminator}``
- ``{author.name_and_discriminator}``
- ``{latency}``

.. _pingoverride-command-pingset-reply:

"""""""""""""
pingset reply
"""""""""""""

**Syntax**

.. code-block:: none

    [p]pingset reply <reply>

**Description**

Set whether the ping message uses replies.

.. _pingoverride-command-pingset-reply-mention:

"""""""""""""""""""""
pingset reply mention
"""""""""""""""""""""

**Syntax**

.. code-block:: none

    [p]pingset reply mention <mention>

**Description**

Set whether the ping message uses replies.

.. _pingoverride-command-pingset-settings:

""""""""""""""""
pingset settings
""""""""""""""""

**Syntax**

.. code-block:: none

    [p]pingset settings

**Description**

See the current settings for PingOverride.

.. _pingoverride-command-pingset-variables:

"""""""""""""""""
pingset variables
"""""""""""""""""

**Syntax**

.. code-block:: none

    [p]pingset variables

.. tip:: Alias: ``pingset vars``

**Description**

List the available variables for the ping command.

.. _quotes:

======
Quotes
======

This is the cog guide for the quotes cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada quotes`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada quotes`

.. _quotes-usage:

-----
Usage
-----

Get a random quote.


.. _quotes-commands:

--------
Commands
--------

.. _quotes-command-quote:

^^^^^
quote
^^^^^

**Syntax**

.. code-block:: ini

    [p]quote

**Description**

Get a random quote.

.. tip::

    We can use bobloy's `FIFO <https://github.com/bobloy/Fox-V3/tree/master/fifo>`_
    cog, with this cog, to run QOTD (Quote of the day).

    **Steps**

    1. ``[p]fifo add qotd quote``
    2. ``[p]fifo addtrigger cron qotd 0 0 * * *``
    3. ``[p]fifo set qotd <feed_channel>``

    Your feed channel is whatever channel you'd like QOTD to be posted in.

.. _raffle:

======
Raffle
======

This is the cog guide for the raffle cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada raffle`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada raffle`

-----
Usage
-----

This cog allows you to create raffles in your guild, with various conditions
to only allow certain users to join them. Raffles can be edited at any time,
and you can learn more about the condition blocks throughout this documentation.

There are simple and complex raffles. Simple raffles simply include a title and
description, and you can pick multiple users until you decide to end it.

Complex raffles, however, are much more complex (as the name says), as you can
implement various conditions to prevent certain users from joining, or certain
requirements such as account age, roles, and more. They are built using YAML -
which is very easy to get started with. Here's a quick peak into what a complex
raffle would look like, and how it's created:

.. code-block:: yaml

    name: "raffle"
    description: "My very first raffle!"
    end_message: "Congrats {winner.mention} - you've won the {raffle} giveaway!"
    roles_needed_to_enter: [749272596050214973, 798947505193746503]
    prevented_users: [766580519000473640]
    maximum_entries: 5
    account_age: 100 # this is in days

This example does not even include all the conditions, and there will definitely
be more conditions coming in the future.

----------------
Condition Blocks
----------------

^^^^
name
^^^^

The name block is the only required key for a raffle. This block must be under 25
characters in length. It will automatically be converted to lowercase, and will have
all spaces removed from it.

This block must be provided as a str (text with quotes).

Please only use alphanumeric characters, with underscores allowed.

^^^^^^^^^^^
description
^^^^^^^^^^^

The description for your raffle. This information appears in the ``[p]raffle info``
command, so people can see what your raffle's about.

This block must be provided as a str (text with quotes)

^^^^^^^^^^^^
join_message
^^^^^^^^^^^^

A block used to personalize a section of the output when using ``[p]raffle join``.
You can use the special arguments of ``{user}``, ``{entry_count}`` and ``{raffle}``
to customize this message so that it has context.

``raffle``:
    The name of the raffle which the user has joined.

``entry_count``:
    The number of entries in the raffle.

``user``:
    The member object of the user who joined the raffle.
    The user variable has various attributes, which
    are self explanatory:

    - user.name
    - user.mention
    - user.id
    - user.display_name
    - user.discriminator
    - user.name_and_discriminator

Make sure to use these variables inside curly brackets (``{}``).

If you want to randomize the join_message, simply provide a list of strings.
Otherwise, provide a string by itself.

^^^^^^^^^^^
end_message
^^^^^^^^^^^

A block used to personalize the draw message when using ``[p]raffle draw``. If this key
is not present, the default message is set to "Congratulations {winner.mention}, you have
won the {raffle} raffle!". You can use the special arguments of ``{winner}`` and ``{raffle}``
to customize this message so that it has context.

``raffle``:
    The name of the raffle which the user has won.

``winner``:
    The member object of the user who won the raffle.
    The winner variable has various attributes, which
    are self explanatory:

    - winner.name
    - winner.mention
    - winner.id
    - winner.display_name
    - winner.discriminator
    - winner.name_and_discriminator

Make sure to use these variables inside curly brackets (``{}``).

If you want to randomize the end_message, this is now an option as of version 1.1.0.
Simply provide a list of strings. Otherwise, provide a string by itself.

.. code-block:: yaml

    # randomised
    end_message: ["Congrats {winner.mention}!", "{winner.name} has won the {raffle} raffle."]
    # selected
    end_message: "Congrats {winner.mention}! You have won my {raffle} raffle."

^^^^^^^^^^^
account_age
^^^^^^^^^^^

The required Discord account age for a user to join. This condition is helpful for reducing
"cheaters" who join on alternate accounts in an attempt to have a greater chance at winning.

This condition must be a number, and it must be provided in days. This number cannot be higher
than the Discord app creation date.

^^^^^^^^^^^^^^^
server_join_age
^^^^^^^^^^^^^^^

The required length of time in days that the user must have been in the server for. This condition
is simular to the ``account_age`` condition, but it is instead how long the user has been in the
server for.

This condition must be a number, and it must be provided in days. This number cannot be higher
than the server's creation date.

.. warning::

    The ``join_age`` condition was deprecated for ``server_join_age`` in version 1.2.3.
    Please update to this version, using ``join_age`` is now unsupported and will not work.

^^^^^^^^^^^^^^^^^^^^^
roles_needed_to_enter
^^^^^^^^^^^^^^^^^^^^^

A list of roles which are required in order to join the raffle. This must be a **list** of
role IDs. In case you were unaware, square brackets (``[]``) are used to denote lists.

.. code-block:: yaml

    # Multiple roles
    roles_needed_to_enter: [749272596050214973, 798947505193746503]
    # One role
    roles_needed_to_enter: [749272596050214973]

^^^^^^^^^^^^^^^^^^^^^^
badges_needed_to_enter
^^^^^^^^^^^^^^^^^^^^^^

A list of badges which are required in order to join the raffle. This must be a **list** of
Discord badges. In case you were unaware, square brackets (``[]``) are used to denote lists.

.. code-block:: yaml

    # Multiple badges
    badges_needed_to_enter: ["verified_bot_developer", "bug_hunter"]
    # One badge
    badges_needed_to_enter: ["staff"]

.. tip::

    Available badges: bug_hunter, bug_hunter_level_2, early_supporter, hypesquad,
    hypesquad_balance, hypesquad_bravery, hypesquad_brilliance, partner, staff,
    system, and verified_bot_developer.

^^^^^^^^^^^^^^^
prevented_users
^^^^^^^^^^^^^^^

A list of users who are not allowed to join the raffle. This must be a **list** of
user IDs. Square brackets (``[]``) are used to denote lists.

^^^^^^^^^^^^^
allowed_users
^^^^^^^^^^^^^

A list of users who are allowed to join the raffle. This must be a **list** of
user IDs. Square brackets (``[]``) are used to denote lists.

^^^^^^^^^^^^^^^
maximum_entries
^^^^^^^^^^^^^^^

The maximum number of entries allowed into the raffle. This condition must be
provided as a number.

^^^^^^^^^^^^^
on_end_action
^^^^^^^^^^^^^

This is the prompt for the bot when the a winner is picked for the raffle through
``[p]raffle draw``. Must be one of the following:

* ``end``: The raffle ends immediately after the first winner is picked.
* ``remove_winner``: The winner is removed from the raffle's entries, but the raffle continues.
* ``remove_and_prevent_winner``: The winner is removed from the raffle's entries, and is added to the prevented list.
* ``keep_winner``: The winner stays in the raffle, and could win again.

If not specified, it defaults to ``keep_winner``.

^^^^^^^^^^^^^^
suspense_timer
^^^^^^^^^^^^^^

This condition allows you to set the time for which the bot types when drawing a winner from the raffle.
This must be provided as a number, and must be between 0 and 10.

.. _raffle-commands:

--------
Commands
--------

Here is a list of all commands available for this cog.
There are 31 in total.

.. _raffle-command-raffle:


^^^^^^
raffle
^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle

**Description**

Manage raffles for your server.

.. _raffle-command-raffle-asyaml:

^^^^^^^^^^^^^
raffle asyaml
^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle asyaml <raffle>

**Description**

Get a raffle in its YAML format.

**Arguments:**
    - `<raffle>` - The name of the raffle to get the YAML for.

.. _raffle-command-raffle-conditions:

^^^^^^^^^^^^^^^^^
raffle conditions
^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle conditions

**Description**

Get information about how conditions work.

.. _raffle-command-raffle-create:

^^^^^^^^^^^^^
raffle create
^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle create

**Description**

Create a raffle.

.. _raffle-command-raffle-create-complex:

^^^^^^^^^^^^^^^^^^^^^
raffle create complex
^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle create complex

**Description**

Create a raffle with complex conditions.

.. _raffle-command-raffle-create-simple:

^^^^^^^^^^^^^^^^^^^^
raffle create simple
^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle create simple <raffle_name> [description]

**Description**

Create a simple arguments with just a name and description.

**Arguments:**
    - `<name>` - The name for the raffle.
    - `[description]` - The description for the raffle.

.. _raffle-command-raffle-docs:

^^^^^^^^^^^
raffle docs
^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle docs

**Description**

Get a link to the docs.

.. _raffle-command-raffle-draw:

^^^^^^^^^^^
raffle draw
^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle draw <raffle>

**Description**

Draw a raffle and select a winner.

**Arguments:**
    - `<raffle>` - The name of the raffle to draw a winner from.

.. _raffle-command-raffle-edit:

^^^^^^^^^^^
raffle edit
^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit

**Description**

Edit the settings for a raffle.

.. _raffle-command-raffle-edit-accage:

^^^^^^^^^^^^^^^^^^
raffle edit accage
^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit accage <raffle> <new_account_age>

**Description**

Edit the account age requirement for a raffle.

Use `0` or `false` to disable this condition.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<new_account_age>` - The new account age requirement.

.. _raffle-command-raffle-edit-allowed:

^^^^^^^^^^^^^^^^^^^
raffle edit allowed
^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit allowed

**Description**

Manage the allowed users list in a raffle.

.. _raffle-command-raffle-edit-allowed-add:

^^^^^^^^^^^^^^^^^^^^^^^
raffle edit allowed add
^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit allowed add <raffle> <member>

**Description**

Add a member to the allowed list of a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<member>` - The member to add to the allowed list.

.. _raffle-command-raffle-edit-allowed-clear:

^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit allowed clear
^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit allowed clear <raffle>

**Description**

Clear the allowed list for a raffle.

.. _raffle-command-raffle-edit-allowed-remove:

^^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit allowed remove
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit allowed remove <raffle> <member>

**Description**

Remove a member from the allowed list of a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<member>` - The member to remove from the allowed list.

.. _raffle-command-raffle-edit-convertsimple:

^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit convertsimple
^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit convertsimple <raffle>

**Description**

Convert a raffle to a simple one (name and description).

**Arguments**
    - ``<raffle>`` - The name of the raffle.

.. _raffle-command-raffle-edit-description:

^^^^^^^^^^^^^^^^^^^^^^^
raffle edit description
^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit description <raffle> <description>

**Description**

Edit the description for a raffle.

Use `0` or `false` to remove this feature.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<description>` - The new description.

.. _raffle-command-raffle-edit-endmessage:

^^^^^^^^^^^^^^^^^^^^^^
raffle edit endmessage
^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit endmessage <raffle> <end_message>

**Description**

Edit the end message of a raffle.

Once you provide an end message, you will have the chance
to add additional messages, which will be selected at random
when a winner is drawn.

Use ``0`` or ``false`` to disable this condition.

**Arguments:**
    - ``<raffle>`` - The name of the raffle.
    - ``<end_message>`` - The new ending message.

.. _raffle-command-raffle-edit-endaction:

^^^^^^^^^^^^^^^^^^^^^
raffle edit endaction
^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit endaction <raffle> <on_end_action>

**Description**

Edit the on_end_action for a raffle.

Use ``0`` or ``false`` to remove this feature.

**Arguments:**
    - ``<raffle>`` - The name of the raffle.
    - ``<on_end_action>`` - The new action. Must be one of ``end``, ``remove_winner``, ``remove_and_prevent_winner``, or ``keep_winner``.

**Arguments:**
    - ``<raffle>`` - The name of the raffle.
    - ``<on_end_action>`` - The new end action.

.. _raffle-command-raffle-edit-fromyaml:

^^^^^^^^^^^^^^^^^^^^
raffle edit fromyaml
^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit fromyaml <raffle>

Edit a raffle directly from yaml.

**Arguments:**
    - `<raffle>` - The name of the raffle to edit.

.. _raffle-command-raffle-edit-joinage:

^^^^^^^^^^^^^^^^^^^
raffle edit joinage
^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit joinage <raffle> <new_join_age>

**Description**

Edit the join age requirement for a raffle.

Use `0` or `false` to disable this condition.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<new_join_age>` - The new join age requirement.

.. _raffle-command-raffle-edit-joinmessage:

^^^^^^^^^^^^^^^^^^^^^^^
raffle edit joinmessage
^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit joinmessage <raffle> <joinmessage>

**Description**

Edit the join message of a raffle.

Once you provide a join message, you will have the chance
to add additional messages, which will be selected at random
when a user enters the raffle.

Use ``0`` or ``false`` to disable this condition.

**Arguments:**
    - ``<raffle>`` - The name of the raffle.
    - ``<join_message>`` - The new joining message.

.. _raffle-command-raffle-edit-maxentries:

^^^^^^^^^^^^^^^^^^^^^^
raffle edit maxentries
^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit maxentries <raffle> <maximum_entries>

**Description**

Edit the max entries requirement for a raffle.

Use `0` or `false` to disable this condition.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<maximum_entries>` - The new maximum number of entries.

.. _raffle-command-raffle-edit-prevented:

^^^^^^^^^^^^^^^^^^
raffle edit badges
^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit badges

**Description**

Manage badge requirements in a raffle.

.. _raffle-command-raffle-edit-badges-add:

^^^^^^^^^^^^^^^^^^^^^^
raffle edit badges add
^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit badges add <raffle> <badges...>

**Description**

Add badge(s) to the badges requirement list.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<badges...>` - The badge(s) to add to the badge requirement list.

.. _raffle-command-raffle-edit-badges-clear:

^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit badges clear
^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit badges clear <raffle>

**Description**

Clear the badge requirements list for a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.

.. _raffle-command-raffle-edit-badges-add:

^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit badges remove
^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit badges remove <raffle> <badges...>

**Description**

Remove badge(s) from the badges requirement list.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<badges...>` - The badge(s) to remove from the badge requirement list.

.. _raffle-command-raffle-edit-prevented:

^^^^^^^^^^^^^^^^^^^^^
raffle edit prevented
^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit prevented

**Description**

Manage prevented users in a raffle.

.. _raffle-command-raffle-edit-prevented-add:

^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit prevented add
^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit prevented add <raffle> <member>

**Description**

Add a member to the prevented list of a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<member>` - The member to add to the prevented list.

.. _raffle-command-raffle-edit-prevented-clear:

^^^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit prevented clear
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit prevented clear <raffle>

**Description**

Clear the prevented list for a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.

.. _raffle-command-raffle-edit-prevented-remove:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit prevented remove
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit prevented remove <raffle> <member>

**Description**

Remove a member from the prevented list of a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<member>` - The member to remove from the prevented list.

.. _raffle-command-raffle-edit-rolesreq:

^^^^^^^^^^^^^^^^^^^^
raffle edit rolesreq
^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit rolesreq

**Description**

Manage role requirements in a raffle.

.. _raffle-command-raffle-edit-rolesreq-add:

^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit rolesreq add
^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit rolesreq add <raffle> <role>

**Description**

Add a role to the role requirements list of a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<role>` - The role to add to the list of role requirements.

.. _raffle-command-raffle-edit-rolesreq-clear:

^^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit rolesreq clear
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit rolesreq clear <raffle>

**Description**

Clear the role requirements list for a raffle.


**Arguments:**
    - `<raffle>` - The name of the raffle.

.. _raffle-command-raffle-edit-rolesreq-remove:

^^^^^^^^^^^^^^^^^^^^^^^^^^^
raffle edit rolesreq remove
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit rolesreq remove <raffle> <role>

**Description**

Remove a role from the role requirements list of a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<role>` - The role to remove from the list of role requirements.

.. _raffle-command-raffle-edit-stimer:

^^^^^^^^^^^^^^^^^^
raffle edit stimer
^^^^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle edit stimer <raffle> <suspense_timer>

**Description**

Edit the suspense timer for a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<suspense_timer>` - The new suspense timer for the raffle.

.. _raffle-command-raffle-end:

^^^^^^^^^^
raffle end
^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle end <raffle>

**Description**

End a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle to end.

.. _raffle-command-raffle-info:

^^^^^^^^^^^
raffle info
^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle info <raffle>

**Description**

Get information about a certain raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle to get information for.

.. _raffle-command-raffle-join:

^^^^^^^^^^^
raffle join
^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle join <raffle>

**Description**

Join a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle to join.

.. _raffle-command-raffle-kick:

^^^^^^^^^^^
raffle kick
^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle kick <raffle> <member>

**Description**

Kick a member from your raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.
    - `<member>` - The member to kick from the raffle.

.. _raffle-command-raffle-leave:

^^^^^^^^^^^^
raffle leave
^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle leave <raffle>

**Description**

Leave a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle to leave.

.. _raffle-command-raffle-list:

^^^^^^^^^^^
raffle list
^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle list

**Description**

List the currently ongoing raffles.

.. _raffle-command-raffle-members:

^^^^^^^^^^^^^^
raffle members
^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle members <raffle>

**Description**

Get all the members of a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle to get the members from.

.. _raffle-command-raffle-mention:

^^^^^^^^^^^^^^
raffle mention
^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle mention <raffle>

**Description**

Mention all the users entered into a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle to mention all the members in.

.. _raffle-command-raffle-parse:

^^^^^^^^^^^^
raffle parse
^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle parse

**Description**

Parse a complex raffle without actually creating it.

.. _raffle-command-raffle-raw:

^^^^^^^^^^
raffle raw
^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle raw <raffle>

**Description**

View the raw dictionary for a raffle.

**Arguments:**
    - `<raffle>` - The name of the raffle.

.. _raffle-command-raffle-refresh:

^^^^^^^^^^^^^^
raffle refresh
^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle refresh

**Description**

Refresh all of the raffle caches.

.. _raffle-command-raffle-teardown:

^^^^^^^^^^^^^^^
raffle teardown
^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle teardown

**Description**

End ALL ongoing raffles.

.. _raffle-command-raffle-template:

^^^^^^^^^^^^^^^
raffle template
^^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle template

**Description**

Get a template of an example raffle.

.. _raffle-command-raffle-version:

^^^^^^^^^^^^^^
raffle version
^^^^^^^^^^^^^^

**Syntax**

.. code-block:: python

    [p]raffle version

**Description**

Get the version of your Raffle cog.

.. _roleboards:

==========
RoleBoards
==========

This is the cog guide for the roleboards cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada roleboards`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada roleboards`

.. _roleboards-usage:

-----
Usage
-----

Get 'leaderboards' about guild roles, such as the users with the most roles,
the roles with the most users, and a full list of all the roles.

.. _roleboards-commands:

--------
Commands
--------

.. _roleboards-command-rb:

^^^^^^^^^
roleboard
^^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]roleboard

**Description**

Get roleboards for this server.

.. _roleboards-command-rb-toproles:

"""""""""""
rb toproles
"""""""""""

**Syntax**

.. code-block:: ini

    [p]rb toproles <index>

**Description**

Get the roles with the most users.

**Arguments**

-   ``<index>``: The number of roles to get the data for.

.. _roleboards-command-rb-topmembers:

"""""""""""""
rb topmembers
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]rb topmembers <index>

**Description**

Get the members with the most roles.

**Arguments**

-   ``<index>``: The number of members to get the data for.

.. _rpsls:

=====
RPSLS
=====

This is the cog guide for the rpsls cog. You will
find detailed docs about usage and commands.

``[p]`` is considered as your prefix.

.. note:: To use this cog, load it by typing this::

        [p]load rpsls

.. _rpsls-usage:

-----
Usage
-----

Rock, paper, scizzors, lizard, spock.

.. image:: /image_rpsls-help.png
    :alt: rlpls help

.. _rpsls-commands:

--------
Commands
--------

.. _rpsls-command-rpsls:

^^^^^
rpsls
^^^^^

**Syntax**

.. code-block:: ini

    [p]rpsls <choice>

**Description**

Play rock, paper, scizzors, lizard, spock.

Use ``[p]rpsls help`` for a diagram.

**Arguments**

* ``<choice>``: Your choice to play. Must be of rock, paper, scissors, lizard, or spock.

.. _spoilerchannel:

==============
SpoilerChannel
==============

This is the cog guide for the spoilerchannel cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add Kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install Kreusada spoilerchannel`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info Kreusada spoilerchannel`

.. _spoilerchannel-usage:

-----
Usage
-----

Set channels to only have spoilers sent in them.


.. _spoilerchannel-commands:

--------
Commands
--------

.. _spoilerchannel-command-spoilerchannel:

^^^^^^^^^^^^^^
spoilerchannel
^^^^^^^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]spoilerchannel

**Description**

Base command for SpoilerChannel.

.. _spoilerchannel-command-spoilerchannel-add:

""""""""""""""""""
spoilerchannel add
""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]spoilerchannel add <channel>

**Description**

Add a channel to the list of spoiler channels.

**Arguments**

* ``<channel>``: A channel to add as a spoiler channel.

.. _spoilerchannel-command-spoilerchannel-clear:

""""""""""""""""""""
spoilerchannel clear
""""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]spoilerchannel clear

**Description**

Clear the spoiler channel list.

.. _spoilerchannel-command-spoilerchannel-list:

"""""""""""""""""""
spoilerchannel list
"""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]spoilerchannel list

**Description**

List all the spoiler channels.

.. _spoilerchannel-command-spoilerchannel-remove:

"""""""""""""""""""""
spoilerchannel remove
"""""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]spoilerchannel remove <channel>

**Description**

Remove a channel from the list of spoiler channels.

**Arguments**

* ``<channel>``: A channel to add as a spoiler channel.

.. _staff:

=====
Staff
=====

This is the cog guide for the staff cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada staff`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada staff`

-----
Usage
-----

This cog will allow you to alert staff using a command, which will be sent
to the specified staff channel. Provides additional details such as the last messages
in the channel, the date, author, and more.

.. _staff-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _staff-command-staff:

^^^^^
staff
^^^^^

**Syntax**

.. code-block:: ini

    [p]staff

**Description**

Alert the staff members.

.. _staff-command-staffset:

^^^^^^^^
staffset
^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]staffset

**Description**

Commands to configure the staff cog.

.. _staff-command-staffset-channel:

""""""""""""""""
staffset channel
""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]staffset channel [channel]

**Description**

Set the channel to receive alerts for staff.

**Arguments**

* ``[channel]``: The channel used for notifications. If none provided, it resets.

.. _staff-command-staffset-role:

"""""""""""""
staffset role
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]staffset role [role]

**Description**

Set the staff role to be pinged for staff alerts.

**Arguments**

* ``[role]``: The staff role. This is optional. If none provided, it resets.

.. _termino:

=======
Termino
=======

This is the cog guide for the termino cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada termino`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada termino`

.. _termino-usage:

-----
Usage
-----

Customize bot shutdown and restart messages, with predicates, too.


.. note:: All commands within this cog are **locked** to bot owner.

.. _termino-commands:

--------
Commands
--------

.. _termino-command-restart:

^^^^^^^
restart
^^^^^^^

**Syntax**

.. code-block:: ini

    [p]restart [silently=False]

**Description**

Attempts to restart Red.

.. _termino-command-shutdown:

^^^^^^^^
shutdown
^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]shutdown [silently=False]

**Description**

Shuts down Red.

.. _termino-command-terminoset:

^^^^^^^^^^
terminoset
^^^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]terminoset

**Description**

Settings for the shutdown and restart commands.

.. _termino-command-terminoset-res:

""""""""""""""
terminoset res
""""""""""""""

**Syntax**

.. code-block:: ini

    [p]terminoset res <restart_message>

.. tip:: Alias: ``terminoset restart``

**Description**

Set and adjust the restart message.

**Arguments**

* ``<restart_message>``: The message to be sent on restarts.

.. _termino-command-terminoset-res-conf:

"""""""""""""""""""
terminoset res conf
"""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]terminoset res conf <true_or_false>

**Description**

Toggle whether restarts confirm before shutting down.

**Arguments**

* ``<true_or_false>``: Whether to toggle or not.

.. _termino-command-terminoset-res-conf:

"""""""""""""""""""""""""""""""
terminoset res restartedmessage
"""""""""""""""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]terminoset restartedmessage <restarted_message>

**Description**

Set the message to be sent after restarting.

The bot will attempt to send this message in the invoked channel.

**Arguments**

* ``<restarted_message>``: The message to send when the bot is back online.

.. _termino-command-terminoset-settings:

"""""""""""""""""""
terminoset settings
"""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]terminoset settings

**Description**

See the current settings for termino.

.. _termino-command-terminoset-shut:

"""""""""""""""
terminoset shut
"""""""""""""""

**Syntax**

.. code-block:: ini

    [p]terminoset shut <shutdown_message>

.. tip:: Alias: ``terminoset shutdown``

**Description**

Set and adjust the shutdown message.

**Arguments**

* ``<shutdown_message>``: The message to be sent on shutdowns.

.. _termino-command-terminoset-shut-conf:

""""""""""""""""""""
terminoset shut conf
""""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]terminoset shut conf <true_or_false>

**Description**

Toggle whether shutdowns confirm before shutting down.

**Arguments**

* ``<true_or_false>``: Whether to toggle or not.

.. _texteditor:

==========
TextEditor
==========

This is the cog guide for the texteditor cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada texteditor`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada texteditor`

.. _texteditor-usage:

-----
Usage
-----

Edit and manipulate with text.


.. _texteditor-commands:

--------
Commands
--------

.. _texteditor-command-editor:

^^^^^^
editor
^^^^^^

**Syntax**

.. code-block:: ini

    [p]editor

**Description**

Base command for editting text.

.. _texteditor-command-editor-alternating:

""""""""""""""""""
editor alternating
""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor alternating <text>

**Description**

Convert the text to alternating case.

.. _texteditor-command-editor-charcount:

""""""""""""""""
editor charcount
""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor charcount [include_spaces=True] <text>

**Description**

Count the number of characters appearing in the text.

.. _texteditor-command-editor-lower:

""""""""""""
editor lower
""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor lower <text>

**Description**

Convert the text to lowercase.

.. _texteditor-command-editor-multiply:

"""""""""""""""
editor multiply
"""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor multiply <multiplier> <text>

**Description**

Multiply the text.

.. _texteditor-command-editor-occurance:

""""""""""""""""
editor occurance
""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor occurance <check> <text>

**Description**

Count how many times something appears in the text.

.. _texteditor-command-editor-remove:

"""""""""""""
editor remove
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor remove <remove> <text>

**Description**

Remove something from the text.

.. _texteditor-command-editor-replace:

""""""""""""""
editor replace
""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor replace <text_to_replace> <replacement> <text>

**Description**

Replace certain parts of the text.

.. _texteditor-command-editor-reverse:

""""""""""""""
editor reverse
""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor reverse <text>

**Description**

Reverse the text.

.. _texteditor-command-editor-shuffle:

""""""""""""""
editor shuffle
""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor shuffle <text>

.. tip:: Alias: ``editor jumble``

**Description**

Completely shuffle the text.

.. _texteditor-command-editor-snake:

""""""""""""
editor snake
""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor snake <text>

**Description**

Convert all spaces to underscores.

.. _texteditor-command-editor-squash:

"""""""""""""
editor squash
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor squash <text>

**Description**

Squash all the words into one.

.. _texteditor-command-editor-title:

""""""""""""
editor title
""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor title <text>

**Description**

Convert the text to titlecase.

.. _texteditor-command-editor-trim:

"""""""""""
editor trim
"""""""""""

**Syntax**

.. code-block:: ini

    [p]editor trim [trimmer= ] <text>

.. tip:: Alias: ``editor strip``

**Description**

Trim the outskirts of the text.

.. _texteditor-command-editor-upper:

""""""""""""
editor upper
""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor upper <text>

**Description**

Convert the text to uppercase.

.. _texteditor-command-editor-wordcount:

""""""""""""""""
editor wordcount
""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]editor wordcount <text>

**Description**

Count the number of words appearing in the text.

.. _timestables:

===========
TimesTables
===========

This is the cog guide for the timestables cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada timestables`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada timestables`

-----
Usage
-----

This cog will allow you to practice your timestables up to 12x12, with stats such as correct, incorrect,
unanswered questions, average time per question, and total time for all questions.

.. _timestables-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _timestables-command-tt:

^^
tt
^^

**Syntax**

.. code-block:: ini

    [p]tt

**Description**

Base command for timestables.

.. _timestables-command-tt-inactive:

"""""""""""
tt inactive
"""""""""""

**Syntax**:

.. code-block:: ini

    [p]tt inactive <questions>

**Description**

Set the number of questions unanswered before the session is automatically
closed due to inactivity.

**Arguments**

* ``<questions>``: The number of questions before the session ends due to inactivity.

.. _timestables-command-tt-settings:

"""""""""""
tt settings
"""""""""""

**Syntax**:

.. code-block:: ini

    [p]tt settings

**Description**

Shows the current settings for times tables.

.. _timestables-command-tt-sleep:

""""""""
tt sleep
""""""""

**Syntax**:

.. code-block:: ini

    [p]tt sleep <seconds>

**Description**

Set the number of seconds between each question.

**Arguments**

* ``<seconds>``: The number of seconds to sleep between each question in seconds.

.. _timestables-command-tt-start:

""""""""
tt start
""""""""

**Syntax**:

.. code-block:: ini

    [p]tt start <number_of_questions>

**Description**

Start playing the timestables game!

**Arguments**

* ``<number_of_questions>``: The number of questions in the round.

.. _timestables-command-tt-time:

"""""""
tt time
"""""""

**Syntax**:

.. code-block:: ini

    [p]tt time

**Description**

Toggles whether time is recorded when you play timestables.

.. _timestables-command-tt-timeout:

""""""""""
tt timeout
""""""""""

**Syntax**:

.. code-block:: ini

    [p]tt timeout <seconds>

**Description**

Sets how long you have to answer each question.

**Arguments**

* ``<seconds>``: The length of time per question in seconds.

.. _vinfo:

=====
Vinfo
=====

This is the cog guide for the vinfo cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada vinfo`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada vinfo`

-----
Usage
-----

This cog will attempt to pull version attributes from modules
and third party cogs and provide you with their version.

.. _vinfo-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _vinfo-command-vinfo:

^^^^^
vinfo
^^^^^

**Syntax**

.. code-block:: ini

    [p]vinfo

**Description**

Get versions of 3rd party cogs, and modules.

.. _vinfo-command-vinfo-cog:

"""""""""
vinfo cog
"""""""""

**Syntax**:

.. code-block:: ini

    [p]vinfo cog <cog>

**Description**

Get's the version of a third party cog. Some author's do not implement
version attributes in their cogs, meaning that this command may not be able to
return a version if it hasn't been defined in the cog's code.

**Arguments**

* ``<cog>``: The cog to get the version from.

.. warning:: The ``<cog>`` **must** be loaded, and provided in the correct case.

**Example Usage**

.. image:: /image_vinfo-cog.png
    :alt: vinfo cog

.. _vinfo-command-vinfo-mod:

"""""""""
vinfo mod
"""""""""

**Syntax**:

.. code-block:: ini

    [p]tt mod <module>

**Description**

Get a module's version information.

**Arguments**

* ``<module>``: The module to get the version from.

.. warning::

    The ``<module>`` **must** be installed, and provided in the correct case.
    There are a few modules such as `Levenshtein`, which start with capitals.

**Example Usage**

.. image:: /image_vinfo-mod.png
    :alt: vinfo mod

.. _votechannel:

===========
VoteChannel
===========

This is the cog guide for the votechannel cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada votechannel`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada votechannel`

-----
Usage
-----

Designate multiple channels to have poll emojis reacted to each
message sent in them.

.. _votechannel-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _votechannel-command-vote:

^^^^
vote
^^^^

**Syntax**

.. code-block:: ini

    [p]vote

**Description**

Commands with votechannel.

.. _votechannel-command-vote-channel:

""""""""""""
vote channel
""""""""""""

**Syntax**

.. code-block:: ini

    [p]vote channel

**Description**

Settings for channels.

.. _votechannel-command-vote-channel-add:

""""""""""""""""
vote channel add
""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]vote channel add <channel>

**Description**

Add a channel to the votechannel list.

**Arguments**

* ``<channel>``: The Discord channel to receive poll reactions for each message sent inside it.

.. _votechannel-command-vote-channel-remove:

"""""""""""""""""""
vote channel remove
"""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]vote channel remove <channel>

**Description**

Remove a channel from the votechannel list.

**Arguments**

* ``<channel>``: The Discord channel to remove from the votechannel list.

.. _votechannel-command-vote-channel-list:

"""""""""""""""""
vote channel list
"""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]vote channel list

**Description**

List the current voting channels.

.. _votechannel-command-vote-emoji:

""""""""""
vote emoji
""""""""""

**Syntax**

.. code-block:: ini

    [p]vote emoji

**Description**

Set and view the current emojis used for votechannel.

.. _votechannel-command-vote-emoji-down:

"""""""""""""""
vote emoji down
"""""""""""""""

**Syntax**

.. code-block:: ini

    [p]vote emoji down [emoji]

**Description**

Sets the downvote emoji for votechannel.

**Arguments**

* ``[emoji]``: The emoji to react with.

.. _votechannel-command-vote-emoji-down:

"""""""""""""
vote emoji up
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]vote emoji up [emoji]

**Description**

Sets the upvote emoji for votechannel.

**Arguments**

* ``[emoji]``: The emoji to react with.

.. _votechannel-command-vote-emoji-presets:

""""""""""""""""""
vote emoji presets
""""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]vote emoji presets

**Description**

Shows the current emojis used for votechannel.

.. _votechannel-command-vote-toggle:

"""""""""""
vote toggle
"""""""""""

**Syntax**

.. code-block:: ini

    [p]vote toggle

**Description**

Toggle votechannel.

.. _yamlscanner:

===========
YamlScanner
===========

This is the cog guide for the yamlscanner cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/Kreusada/Kreusada-Cogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada yamlscanner`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada yamlscanner`

.. _yamlscanner-usage:

-----
Usage
-----

An easy and quick tool to validate yaml.


.. _yamlscanner-commands:

--------
Commands
--------

.. _yamlscanner-command-yamlscan:

^^^^^^^^
yamlscan
^^^^^^^^

**Syntax**

.. code-block:: ini

    [p]yamlscan

**Description**

Scan yaml to see if its correct.

Your next message will be used to as the yaml to scan.
You can also upload a YAML file.
