function deleteNote(nodeId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ nodeId: nodeId }),
  }).then((res) => (window.location.href = "/"));
}
