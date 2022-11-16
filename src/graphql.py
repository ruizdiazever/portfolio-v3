from typing import List
from strawberry import field, type
import strawberry
from src.views.blog import Blog, get_post, get_blog, create_post
from src.views.article import Article, get_article
from src.views.about import About, get_about
from src.views.project import Project, get_projects


@type
class Query:
    post: Blog = field(resolver=get_post)
    blog: List[Blog] = field(resolver=get_blog)
    article: Article = field(resolver=get_article)
    about: About = field(resolver=get_about)
    project: List[Project] = field(resolver=get_projects)


@type
class Mutation:
    create_post: str = strawberry.mutation(resolver=create_post)
