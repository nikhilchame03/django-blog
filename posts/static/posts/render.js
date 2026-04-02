async function helper() {
  let res = await fetch("api/graphql/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      query: `query { posts { id title createdAt body } }`
    })
  });

  // async function helper() { 
  //   let res = await fetch("/api/posts/"); 
  //   let posts = await res.json();

  let json = await res.json();
  let posts = json.data.posts;

  let search = new URLSearchParams(window.location.search).get("search");
  if (search) {
    posts = posts.filter(p => p.title.toLowerCase().includes(search.toLowerCase()));
  }

  let box = document.getElementById("posts");
  box.innerHTML = "";

  for (let i = 0; i < posts.length; i++) {
    let p = posts[i];
    box.innerHTML += `
      <div class="card">
        <a href="/post/${p.id}">
          <h2>${p.title}</h2>
          <h5>${new Date(p.createdAt).toLocaleString("en-IN")}</h5>
          <p>${p.body.split(" ").slice(0,20).join(" ")}...</p>
        </a>
      </div>
    `;
  }
}

window.onload = helper;
