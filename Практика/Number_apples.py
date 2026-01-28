# Максим взял в школу n яблок. k яблок он отдал друзьям, еще 1 яблоко отдал учителю. Напишите программу, которая посчитает сколько яблок осталось у Максима

apples = int(input())
apples_del = int(input())
res_apps = apples - apples_del
print(res_apps - 1)