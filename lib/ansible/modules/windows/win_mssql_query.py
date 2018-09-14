#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Jon Hawkesworth (@jhawkesworth) <figs@unity.demon.co.uk>
# Copyright: (c) 2017, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'core'}

DOCUMENTATION = r'''
---
module: win_mssql_query
version_added: '1.9.2'
short_description: Copies files to remote locations on windows hosts
description:
- The C(win_mssql_query) module copies a file on the local box to remote windows locations.
options:
  content:
    description:
    - When used instead of C(src), sets the contents of a file directly to the
      specified value. This is for simple values, for anything complex or with
      formatting please switch to the template module.
    version_added: '2.3'
  decrypt:
    description:
    - This option controls the autodecryption of source files using vault.
    type: bool
    default: 'yes'
    version_added: '2.5'
  dest:
    description:
    - Remote absolute path where the file should be copied to. If src is a
      directory, this must be a directory too.
    - Use \ for path separators or \\ when in "double quotes".
    - If C(dest) ends with \ then source or the contents of source will be
      copied to the directory without renaming.
    - If C(dest) is a nonexistent path, it will only be created if C(dest) ends
      with "/" or "\", or C(src) is a directory.
    - If C(src) and C(dest) are files and if the parent directory of C(dest)
      doesn't exist, then the task will fail.
    required: yes
    type: path
  force:
    description:
    - If set to C(yes), the file will only be transferred if the content
      is different than destination.
    - If set to C(no), the file will only be transferred if the
      destination does not exist.
    - If set to C(no), no checksuming of the content is performed which can
      help improve performance on larger files.
    type: bool
    default: 'yes'
    version_added: '2.3'
  local_follow:
    description:
    - This flag indicates that filesystem links in the source tree, if they
      exist, should be followed.
    type: bool
    default: 'yes'
    version_added: '2.4'
  remote_src:
    description:
    - If C(no), it will search for src at originating/master machine.
    - If C(yes), it will go to the remote/target machine for the src.
    type: bool
    default: 'no'
    version_added: '2.3'
  src:
    description:
    - Local path to a file to copy to the remote server; can be absolute or
      relative.
    - If path is a directory, it is copied (including the source folder name)
      recursively to C(dest).
    - If path is a directory and ends with "/", only the inside contents of
      that directory are copied to the destination. Otherwise, if it does not
      end with "/", the directory itself with all contents is copied.
    - If path is a file and dest ends with "\", the file is copied to the
      folder with the same filename.
    required: yes
    type: path
notes:
- For non-Windows targets, use the M(copy) module instead.
- Currently win_mssql_query does not support copying symbolic links from both local to
  remote and remote to remote.
- It is recommended that backslashes C(\) are used instead of C(/) when dealing
  with remote paths.
- Because win_mssql_query runs over WinRM, it is not a very efficient transfer
  mechanism. If sending large files consider hosting them on a web service and
  using M(win_get_url) instead.
author:
- Jon Hawkesworth (@jhawkesworth)
- Jordan Borean (@jborean93)
'''

EXAMPLES = r'''
- name: Execute a query on sql server
  win_mssql_query:
    serverinstance: 
    database:
    query:
    authentication:
    username:
    password:
    timeout:
'''

RETURN = r'''
dest:
    description: destination file/path
    returned: changed
    type: string
'''
