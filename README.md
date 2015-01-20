# This is Simple Backup

It's a simple set of scripts that leverage [duplicity](http://duplicity.nongnu.org) to do file backups to S3. It might even work with other destinations, but that's not tested.

To get started, copy the etc/settings.template to etc/settings and edit to your requirements.
Edit etc/sets, to contain the locations to backup, one per line. Backups are recursive.

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

Create a bucket, $BUCKET

Create a new IAM user, $BACKUPUSER, with the following policy. Generate
access keys

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
        "arn:aws:s3:::$BUCKET/*",
        "arn:aws:s3:::$BUCKET"
      ],
      "Effect": "Allow"
    }
  ]
}
```

# License

LGPLv3

# Author

Matt Willsher <matt@willsher.systems>

&copy; 2015 Willsher Systems

