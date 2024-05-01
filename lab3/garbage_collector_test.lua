local busted = require("busted")
local assert = require("luassert")

describe("Garbage Collector Test", function()
    it("Should collect garbage and reduce memory usage", function()
        local memory_usage_before = collectgarbage("count")

        for i = 1, 1000 do
            local data = {}
            for j = 1, 100 do
                data[j] = tostring(math.random(1, 100))
            end
        end

        local memory_usage_after = collectgarbage("count")

        assert.is_less_than(memory_usage_after, memory_usage_before)
    end)
end)