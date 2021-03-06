# Copyright 2013 OpenStack Foundation
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4


from oslo.config import cfg

from manila.openstack.common import log as logging


CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class FakeVolume(object):
    def __init__(self, **kwargs):
        self.id = kwargs.pop('id', 'fake_vol_id')
        self.status = kwargs.pop('status', 'available')
        self.device = kwargs.pop('device', '')
        self.display_name = kwargs.pop('display_name', 'fake_vol_name')
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, attr):
        return getattr(self, attr)


class FakeVolumeSnapshot(object):
    def __init__(self, **kwargs):
        self.id = kwargs.pop('id', 'fake_volsnap_id')
        self.status = kwargs.pop('status', 'available')
        self.display_name = kwargs.pop('display_name', 'fake_volsnap_name')
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, attr):
        return getattr(self, attr)


class API(object):
    """Fake Volume API."""
    def get(self, volume_id):
        pass

    def create_snapshot_force(self, *args, **kwargs):
        pass

    def get_snapshot(self, *args, **kwargs):
        pass

    def delete_snapshot(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass

    def get_all(self, search_opts):
        pass

    def delete(self, volume_id):
        pass

    def get_all_snapshots(self, search_opts):
        pass
