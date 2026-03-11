from django import template

register = template.Library()


@register.filter
def split_tags(value):
    """Split a comma-separated string into a list."""
    if not value:
        return []
    return [tag.strip() for tag in value.split(',') if tag.strip()]


@register.filter
def is_video(url):
    """Check if a URL points to a video file."""
    if not url:
        return False
    return url.lower().endswith(('.mp4', '.webm', '.ogg'))
