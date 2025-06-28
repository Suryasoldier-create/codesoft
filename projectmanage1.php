$sql = "UPDATE tasks SET status='In Progress' WHERE id IN (SELECT task_id FROM subtasks WHERE status='Completed')";
$conn->query($sql);

function decryptData($data, $key) {
    return openssl_decrypt($data, 'AES-256-CBC', $key, 0, 'your_iv');
}

