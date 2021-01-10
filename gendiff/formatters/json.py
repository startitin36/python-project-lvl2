def form_view(diff):
    result = ['{']
    for key in sorted(diff.keys()):
        result.append('{}: {}'.format(key, diff[key]))
    return '\n'.join(result)
