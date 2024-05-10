local busted = require("busted")
local assert = require("luassert")

describe("Lua Numbers Creation on Stack Test", function()
    it("Should demonstrate nums creation on the stack", function()

        local memory_before = collectgarbage('count')

        local num = 1

        num = nil

        collectgarbage()


        assert.is_true(collectgarbage('count') < memory_before)
    end)
end)