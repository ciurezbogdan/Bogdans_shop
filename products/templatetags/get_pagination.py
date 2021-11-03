from django import template

register = template.Library()


@register.filter(name='pagination_url')
def get_pagination_url(request, page_number=1):
    encoded_url = request.GET.urlencode() or ''
    old_page = request.GET.get('page')
    if old_page:
        encoded_url = encoded_url.replace('?', '').replace('page=%s' % old_page, '')
    print('encoded_url')

    if encoded_url:
        if encoded_url[-1] == '&':
            encoded_url = encoded_url[:-1]
        return '?%s&page=%s' % (encoded_url, page_number)

    return '?page=%s' % page_number


@register.filter(name='visible_pages')
def visible_pages(page_obj):
    paginator = page_obj.paginator
    pages = list(paginator)
    current_page = page_obj.number
    first_pages = pages[0:2]
    last_pages = pages[-2:]

    if current_page == 1 or current_page == paginator.num_pages:
        return first_pages + [None] + last_pages

    current_page_index = [page.number for page in pages].index(current_page)
    return first_pages + [None] + pages[current_page_index-1:current_page_index+2] + [None] + last_pages
