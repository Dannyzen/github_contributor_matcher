#!/usr/bin/env python3
from github3 import login, exceptions
from sys import argv
from os import getenv


def loadGithubToken():
    # Pull 'key' in from env var "GITHUB_TOKEN", else, maybe there's a config.yaml with a 'key'
    if getenv("GITHUB_TOKEN") is not None:
        github_token = getenv("GITHUB_TOKEN")
    else:
        try:
            from yaml import load, YAMLError
            yaml_blob = load(file('./config.yaml','r'))
            github_token = yaml_blob['token']
        except (IOError, NameError):
            print("Attempted to load a github token. Tried to use the environmental variable 'GITHUB_TOKEN', then tried to load a config.yaml. Neither were found. Read the README.")
            raise
    global github
    github = login(token=github_token)

def getOrgId(org_str = argv[1]):
    """ Given an org that I want to search (first argument), get the org ID"""
    try:
        org_obj = github.organization(org_str)
    except exceptions.NotFoundError:
        print("Unable to find find the organization {organization} in Github, try another organization name.".format(organization=org_str))
        raise
    return org_obj.id

def matchCompanyWithRepo(owner_org = argv[2], repo_name = argv[3]):
    try:
        repo = github.repository(owner_org, repo_name)
    except exceptions.NotFoundError:
        print("Unable to find the repository {owner_org}/{repo_name} in Github, try another repository name.".format(owner_org=owner_org, repo_name=repo_name))
        raise
    org_id = getOrgId()
    print("Searching {owner_org}/{repo_name} for all users in the {org} organization".format(owner_org=owner_org, repo_name=repo_name, org=argv[1]))
    for user_contributor in repo.contributors():
        contributor_orgs = github.organizations_with(user_contributor.login)
        for contributors_org in contributor_orgs:
            if contributors_org.id == org_id:
                user = github.user(user_contributor)
                print("User: {login}, Name: {name}, Email: {email}, Company: {company}".format(login=user.login, name=user.name, email=user.email, company=user.company))

def main():
    loadGithubToken()
    matchCompanyWithRepo()

if __name__ == '__main__':
    main()
