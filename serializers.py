from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from miningusage.models import WebPageIdentifier, WebPage, Sequence, WebSite, Domain


class WebpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = ('url', 'pageStructure', 'Xpath', 'CSSPath1', 'CSSPath2', 'BrowserSess', 'command', 'linkText',
                  'keyTypes', 'XpathDragPath', 'XpathDropPath', 'recordedKeystrokes')


class WebSiteSerializer(ModelSerializer):
    class Meta:
        model = WebSite
        fields = ['name', ]


class DomainSerializer(ModelSerializer):
    class Meta:
        model = Domain
        fields = ['domain', 'webSite']


class WebPageIdentifierSerializer(ModelSerializer):
    def validate(self, attrs):
        if attrs['similarityMethod'] not in [c[0] for c in WebPageIdentifier.SimilarityMethods.choices]:
            raise serializers.ValidationError("Similarity method does not exist")
        return attrs

    class Meta:
        model = WebPageIdentifier
        fields = ['similarityMethod', ]


class WebPageListSerializer(ModelSerializer):
    class Meta:
        model = WebPage
        fields = ['url']


class WebPageIdentifierListSerializer(ModelSerializer):
    webPages = WebPageListSerializer(many=True, read_only=True)

    class Meta:
        model = WebPageIdentifier
        fields = ['pk', 'similarityMethod', 'webPages']


class SequenceSerializer(ModelSerializer):
    class Meta:
        model = Sequence
        fields = ['support', 'webPageIdentifiers']
