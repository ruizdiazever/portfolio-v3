# GraphQL

## Querys

Fields

```graphql
query Blog {
  blog {
    title
  }
}

query Post {
  post (id: 2) {
    title, subtitle
  }
}
```

Mutation

```graphql
# QUERY
mutation CreatePost(
  $title: String!, 
  $subtitle: String!,
  $description: String!,
  $date: DateTime!,
  $updated: DateTime!,
  $position: Int!){
  createPost(
    title: $title, 
    subtitle: $subtitle, 
    description: $description,
    date: $date,
    updated: $updated,
    position: $position
  )
}

# Variables
{
  "title": "Hello GraphQL",
  "subtitle": "FastAPI + Svelte from GraphQL",
  "description": "", 
  "date": "2022-11-05 02:11:35", 
  "updated": "2022-11-05 02:11:35", 
  "position": 2
}
```
