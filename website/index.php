<html>

<head>
    <title>SUPMIT</title>
</head>

<body>
    <h1>Student Checking App</h1>
    <form action="" method="POST">
        <button type="submit" name="submit">List Student</button>
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] == "POST" && isset($_POST['submit'])) {
        // Use environment variables or default credentials
        $username = $_ENV['USERNAME'] ?? 'root';
        $password = $_ENV['PASSWORD'] ?? 'root';

        $context = stream_context_create([
            "http" => [
                "header" => "Authorization: Basic " . base64_encode("$username:$password"),
                "timeout" => 5 // Timeout to prevent hanging
            ]
        ]);

        $url = 'http://student_api:3000/supmit/api/v1.0/get_student_ages';
        $response = file_get_contents($url, false, $context);

        if ($response === FALSE) {
            echo "<p style='color:red;'>Failed to retrieve student data. API might be down.</p>";
        } else {
            $list = json_decode($response, true);
            echo "<p style='color:red; font-size: 20px;'>This is the list of students with their ages:</p>";
            foreach ($list["student_ages"] as $key => $value) {
                echo "- <b>$key</b> is <b>$value</b> years old <br>";
            }
        }
    }
    ?>
</body>

</html>