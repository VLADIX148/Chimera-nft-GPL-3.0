# Copyright (C) 2026 Anonymous
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

LEGACY_GIFT_REGISTRY = {
    # base_gift_id: metadata
    # Extend this map as more historical gifts need dedicated labels/styles.
}


def get_legacy_gift_meta(base_gift_id=0):
    try:
        gid = int(base_gift_id or 0)
    except Exception:
        gid = 0
    if gid <= 0:
        return {}
    raw = LEGACY_GIFT_REGISTRY.get(gid)
    if not isinstance(raw, dict):
        return {}
    return dict(raw)
