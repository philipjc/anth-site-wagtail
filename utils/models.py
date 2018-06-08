from django.db import models
from wagtail.core.blocks import StructBlock, RichTextBlock, StreamBlock

# Create your models here.


class ContentBlock(StructBlock):
    content = RichTextBlock()


class GeneralStreamBlock(StreamBlock):
    content = ContentBlock(icon="pilcrow", label="Single Column")
