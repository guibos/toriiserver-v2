```
query {
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