import json
from urllib.request import urlopen


def retrieve_tag_info(tag_name, repository_url):
    """
    Retrieves tag information from distant API.

    Since the GitHub API is paginated, (*i.e.* it does not list all data in a single page,
    but rather serves pages holding 30 elements maximum), we need to browse all pages
    until either the tag is found or the page is empty, meaning we didn't find the tag.
    Page browsing is done by updating the `page` URL argument (`?page=1`, `?page=2` etc).

    @param tag_name: the name of the mod release
    @param repository_url: API URL used to access mod's tags data
    @return: tag data, including commit SHA signature
    """

    api_link = build_tags_url(repository_url)

    i = 1
    while True:
        url = f'{api_link}?page={i}'
        response = urlopen(url)
        tags_data = json.loads(response.read())

        # If page is empty, it means the tag couldn't be found
        if len(tags_data) == 0:
            print("Tag not found.")
            return None

        # If there's one matching result, we found the tag!
        matching_distant_versions = list(filter(lambda v: v['name'] == tag_name, tags_data))
        if len(matching_distant_versions) == 1:
            return matching_distant_versions[0]
        i += 1


def build_tags_url(repository_url):
    words = repository_url.split('/')
    return f"https://api.github.com/repos/{words[-2]}/{words[-1]}/tags"


def get_commit_hash(info):
    return info['commit']['sha']
