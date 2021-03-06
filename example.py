# Copyright 2013 TellApart, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# =============================================================================
#
# Example usage of commandr.
#

from commandr import command, Run

@command('greet')
def SayGreeting(name, title='Mr.', times=1, comma=False, capslock=False):
  """Greet someone.

  Arguments:
    name - Name to greet.
    title - Title of the person to greet.
    times - Number of time to say the greeting.
    comma - Whether to add a comma after the greeting.
    capslock - Whether to output in ALL CAPS.
  """
  message = 'Hi%s %s %s!' % (',' if comma else '', title, name)
  if capslock:
    message = message.upper()

  for _ in xrange(times):
    print message

if __name__ == '__main__':
  Run()
