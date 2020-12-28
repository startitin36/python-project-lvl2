def form_view(diff):
    result = '{'
    for key in sorted(diff.keys()):
        result += '\n{}: {}'.format(key, diff[key])
    return result
