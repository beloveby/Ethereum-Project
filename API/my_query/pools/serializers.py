# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 21:02
# @Author  : Yuan Bian
# @File    : serializers.py
from rest_framework import serializers
from pools.models import Pool


class PoolSerializer(serializers.Serializer):
    field = serializers.URLField()
    account = serializers.CharField(max_length=100, default='')
    password = serializers.CharField(max_length=100, default='')
    info = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Pool` instance, given the validated data.
        """
        return Pool.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Pool` instance, given the validated data.
        """
        instance.field = validated_data.get('code', instance.field)
        instance.account = validated_data.get('account', instance.account)
        instance.password = validated_data.get('password', instance.password)
        instance.info = validated_data.get('info', instance.info)
        instance.save()
        return instance