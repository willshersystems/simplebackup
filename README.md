# This is Simple backup

To get started, copy the etc/settings.template to etc/settings and edit to your requirements.

## Commands

| Command          | Action                                      |
| ---------------- | ------------------------------------------- |
| backup_check     | Run collection-status again each backup set |
| backup_clean     | Removed old backups from S3                 |
| backup_list      | list-current-files for each set             |
| backup_restore   | restore the give path to $path.RESTORED     |
| backup_sets      | list the backup sets                        |
| backup_totalsize | reports the total size of backup data in S3 |
| backup_verify    | verify the backup sets against local data   |

## S3 set up

Create a bucket, `$CLIENTNAME.backups.willsher.systems`

Create a new IAM user, with the following policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListObject",
        "s3:ListBucket",
        "s3:DeleteObject"
      ],
      "Sid": "Stmt1379794867000",
      "Resource": [
        "arn:aws:s3:::$CLIENTNAME.backups.willsher.systems/*",
        "arn:aws:s3:::$CLIENTNAME.backups.willsher.systems"
      ],
      "Effect": "Allow"
    }
  ]
}
```
