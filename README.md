```query {
  users {
    edges {
      node {
        id
        username
        titles {
          edges {
            node {
              id,
              name
            }
          }
        }
      }
    }
  }
}```

```mutation {
  createUser(userData: {username: "Fuckencio"}) {
    user {
      username
    }
  }
}```

mutation {createUser(input: {username: "Fuckencio"}) {user {username}}}


```curl -X POST http://127.0.0.1:5000/graphql/ \
     -H 'content-type: multipart/form-data; boundary=----GraphQlFileUpload' \
     -F 'query=mutation {createUser(userData: {username: "Fuckencio"}) {user {username}}}' \
     -F 'photo=@run.py'
```