from datetime import datetime, timedelta

import requests


class GitService:
    URL = 'https://api.github.com'

    def get_access_token(self, user):
        return user.social_auth.get(provider='github').extra_data['access_token']

    def get_headers(self, user):
        token = self.get_access_token(user)
        return {
            'content-type': 'application/json; charset=utf-8',
            'authorization': f'token {token}'
        }

    def get_user_repositories(self, user):
        owner = user.social_auth.get(provider='github').extra_data['login']
        repo_request = requests.get(
            f'{self.URL}/users/{owner}/repos',
            headers=self.get_headers(user)
        )
        if repo_request:
            return [{
                'full_name': repos['full_name'],
                'name': repos['name']
            } for repos in repo_request.json()]
        return repo_request

    def get_repository(self, repository, owner, user):
        if owner == user.social_auth.get(provider='github').extra_data['login']:
            repo_request = requests.get(
                f'{self.URL}/repos/{owner}/{repository}',
                headers=self.get_headers(user)
            )
            if repo_request:
                return repo_request.json()
            return repo_request
        return None

    def get_username_from_url(self, url):
        return url.split('/')[-1]

    def get_repository_commits(self, repository, owner, user):
        payload = {'since': datetime.today() - timedelta(days=30)}
        commits_request = requests.get(
            f'{self.URL}/repos/{owner}/{repository}/commits',
            params=payload,
            headers=self.get_headers(user)
        )
        if commits_request:
            return [{
                'sha': commit['sha'],
                'author': self.get_username_from_url(commit['author']['url']),
                'message': commit['commit']['message'],
                'date': commit['commit']['author']['date']
            } for commit in commits_request.json()]
        return commits_request

    def set_repository_webhook(self, repository, owner, user, url):
        payload = {
            "events": [
                "push",
            ],
            "config": {
                "url": url,
                "content_type": "json"
            }
        }
        requests.post(
            f'{self.URL}/repos/{owner}/{repository}/hooks',
            headers=self.get_headers(user),
            json=payload
        )
