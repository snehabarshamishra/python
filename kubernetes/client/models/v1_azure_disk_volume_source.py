# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1AzureDiskVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'caching_mode': 'str',
        'disk_name': 'str',
        'disk_uri': 'str',
        'fs_type': 'str',
        'kind': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'caching_mode': 'cachingMode',
        'disk_name': 'diskName',
        'disk_uri': 'diskURI',
        'fs_type': 'fsType',
        'kind': 'kind',
        'read_only': 'readOnly'
    }

    def __init__(self, caching_mode=None, disk_name=None, disk_uri=None, fs_type=None, kind=None, read_only=None):
        """
        V1AzureDiskVolumeSource - a model defined in Swagger
        """

        self._caching_mode = None
        self._disk_name = None
        self._disk_uri = None
        self._fs_type = None
        self._kind = None
        self._read_only = None
        self.discriminator = None

        if caching_mode is not None:
          self.caching_mode = caching_mode
        self.disk_name = disk_name
        self.disk_uri = disk_uri
        if fs_type is not None:
          self.fs_type = fs_type
        if kind is not None:
          self.kind = kind
        if read_only is not None:
          self.read_only = read_only

    @property
    def caching_mode(self):
        """
        Gets the caching_mode of this V1AzureDiskVolumeSource.
        Host Caching mode: None, Read Only, Read Write.

        :return: The caching_mode of this V1AzureDiskVolumeSource.
        :rtype: str
        """
        return self._caching_mode

    @caching_mode.setter
    def caching_mode(self, caching_mode):
        """
        Sets the caching_mode of this V1AzureDiskVolumeSource.
        Host Caching mode: None, Read Only, Read Write.

        :param caching_mode: The caching_mode of this V1AzureDiskVolumeSource.
        :type: str
        """

        self._caching_mode = caching_mode

    @property
    def disk_name(self):
        """
        Gets the disk_name of this V1AzureDiskVolumeSource.
        The Name of the data disk in the blob storage

        :return: The disk_name of this V1AzureDiskVolumeSource.
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        """
        Sets the disk_name of this V1AzureDiskVolumeSource.
        The Name of the data disk in the blob storage

        :param disk_name: The disk_name of this V1AzureDiskVolumeSource.
        :type: str
        """
        if disk_name is None:
            raise ValueError("Invalid value for `disk_name`, must not be `None`")

        self._disk_name = disk_name

    @property
    def disk_uri(self):
        """
        Gets the disk_uri of this V1AzureDiskVolumeSource.
        The URI the data disk in the blob storage

        :return: The disk_uri of this V1AzureDiskVolumeSource.
        :rtype: str
        """
        return self._disk_uri

    @disk_uri.setter
    def disk_uri(self, disk_uri):
        """
        Sets the disk_uri of this V1AzureDiskVolumeSource.
        The URI the data disk in the blob storage

        :param disk_uri: The disk_uri of this V1AzureDiskVolumeSource.
        :type: str
        """
        if disk_uri is None:
            raise ValueError("Invalid value for `disk_uri`, must not be `None`")

        self._disk_uri = disk_uri

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1AzureDiskVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.

        :return: The fs_type of this V1AzureDiskVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1AzureDiskVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.

        :param fs_type: The fs_type of this V1AzureDiskVolumeSource.
        :type: str
        """

        self._fs_type = fs_type

    @property
    def kind(self):
        """
        Gets the kind of this V1AzureDiskVolumeSource.
        Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared

        :return: The kind of this V1AzureDiskVolumeSource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1AzureDiskVolumeSource.
        Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared

        :param kind: The kind of this V1AzureDiskVolumeSource.
        :type: str
        """

        self._kind = kind

    @property
    def read_only(self):
        """
        Gets the read_only of this V1AzureDiskVolumeSource.
        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :return: The read_only of this V1AzureDiskVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1AzureDiskVolumeSource.
        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :param read_only: The read_only of this V1AzureDiskVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1AzureDiskVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
